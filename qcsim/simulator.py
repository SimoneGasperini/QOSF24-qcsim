import sympy
import numpy


class Simulator:

    def __init__(self):
        pass

    def _init_statetensor(self, num_qubits):
        state = numpy.zeros((2,) * num_qubits)
        state[(0,) * num_qubits] = 1
        self._statetensor = sympy.Array(state)

    def _apply_1q_gate(self, gate):
        gate_tensor = gate.matrix
        i = -gate.qubit - 1
        self._statetensor = numpy.tensordot(
            gate_tensor, self._statetensor, axes=(1, i))
        self._statetensor = numpy.moveaxis(self._statetensor, 0, i)

    def _apply_2q_gate(self, gate):
        gate_tensor = gate.matrix.reshape(2, 2, 2, 2)
        c = -gate.control - 1
        t = -gate.target - 1
        self._statetensor = numpy.tensordot(
            gate_tensor, self._statetensor, axes=((2, 3), (c, t)))
        self._statetensor = numpy.moveaxis(self._statetensor, (0, 1), (c, t))

    def run(self, circuit):
        self._init_statetensor(circuit.num_qubits)
        for gate in circuit._data:
            if gate.num_qubits == 1:
                self._apply_1q_gate(gate)
            elif gate.num_qubits == 2:
                self._apply_2q_gate(gate)

    def get_statevector(self):
        num_qubits = len(self._statetensor.shape)
        psi = self._statetensor.reshape(2**num_qubits)
        return numpy.array(psi, dtype=complex)
