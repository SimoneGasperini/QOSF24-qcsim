import functools
import numpy as np


class Simulator:

    def __init__(self):
        pass

    def _init_statevector(self, num_qubits):
        zeros = [np.array([1, 0])] * num_qubits
        self._statevector = functools.reduce(np.kron, zeros)

    def run(self, circuit):
        self._init_statevector(num_qubits=circuit.num_qubits)
        for layer in circuit._data:
            matrices = [gate.matrix for gate in layer[::-1]
                        if gate is not None]
            operator = functools.reduce(np.kron, matrices)
            self._statevector = operator @ self._statevector

    def get_statevector(self):
        return self._statevector
