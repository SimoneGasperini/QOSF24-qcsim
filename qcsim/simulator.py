import functools
import collections
import random
import numpy as np
from qcsim.gates import I


class Simulator:

    def __init__(self, method):
        # method: "matrix-mul" or "tensor-mul"
        self.method = method

    def _init_statevector(self, num_qubits):
        state = np.zeros(2**num_qubits)
        state[0] = 1
        self._statevector = state

    def _init_statetensor(self, num_qubits):
        state = np.zeros((2,) * num_qubits)
        state[(0,) * num_qubits] = 1
        self._statetensor = state

    def _run_matrix_mul(self, circuit):
        # 1) Naive simulation using matrix multiplication
        self._init_statevector(circuit.num_qubits)
        for layer in circuit._data:
            matrices = [gate.matrix for gate in layer[::-1]
                        if gate is not None]
            operator = functools.reduce(np.kron, matrices)
            self._statevector = operator @ self._statevector

    def _apply_1q_gate(self, gate):
        gate_tensor = gate._matrix
        i = -gate.qubit - 1
        self._statetensor = np.tensordot(
            gate_tensor, self._statetensor, axes=(1, i))
        self._statetensor = np.moveaxis(self._statetensor, 0, i)

    def _apply_2q_gate(self, gate):
        gate_tensor = gate._matrix.reshape(2, 2, 2, 2)
        c = -gate.control - 1
        t = -gate.target - 1
        self._statetensor = np.tensordot(
            gate_tensor, self._statetensor, axes=((2, 3), (c, t)))
        self._statetensor = np.moveaxis(self._statetensor, (0, 1), (c, t))

    def _run_tensor_mul(self, circuit):
        # 2) Advanced simulation using tensor multiplication
        self._init_statetensor(circuit.num_qubits)
        gates = [gate for layer in circuit._data for gate in layer
                 if gate is not None and not isinstance(gate, I)]
        for gate in gates:
            if gate.num_qubits == 1:
                self._apply_1q_gate(gate)
            elif gate.num_qubits == 2:
                self._apply_2q_gate(gate)

    def run(self, circuit):
        if self.method == 'matrix-mul':
            self._run_matrix_mul(circuit)
        elif self.method == 'tensor-mul':
            self._run_tensor_mul(circuit)

    def get_statevector(self):
        if self.method == 'matrix-mul':
            psi = self._statevector
        elif self.method == 'tensor-mul':
            psi = self._statetensor.flatten()
        return psi

    def sample(self, num_shots):
        # 3) Bonus question: sampling statevector
        psi = self.get_statevector()
        num_qubits = int(np.log2(len(psi)))
        states = [np.binary_repr(i, width=num_qubits)
                  for i in range(2**num_qubits)]
        probs = np.square(np.abs(psi))
        samples = random.choices(states, weights=probs, k=num_shots)
        return dict(collections.Counter(samples))

    def expval(self, observable):
        # 3) Bonus question: computing exact expectation values
        if not np.all(observable == observable.conj().T):  # hermitian matrix
            error_message = 'The given observable must be an Hermitian matrix!'
            raise ValueError(error_message)
        ket = self.get_statevector()
        bra = ket.conj().T
        return float(bra @ observable @ ket)
