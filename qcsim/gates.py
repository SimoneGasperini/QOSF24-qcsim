import functools
import numpy as np


class I:
    num_qubits = 1
    _matrix = np.array([[1, 0],
                        [0, 1]])

    def __init__(self, qubit):
        self.qubit = qubit

    @property
    def matrix(self):
        return self._matrix


class X:
    num_qubits = 1
    _matrix = np.array([[0, 1],
                        [1, 0]])

    def __init__(self, qubit):
        self.qubit = qubit

    @property
    def matrix(self):
        return self._matrix


class H:
    num_qubits = 1
    _matrix = 1/np.sqrt(2) * np.array([[1, 1],
                                       [1, -1]])

    def __init__(self, qubit):
        self.qubit = qubit

    @property
    def matrix(self):
        return self._matrix


class CNOT:
    num_qubits = 2
    _matrix = np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 1],
                        [0, 0, 1, 0]])

    def __init__(self, control, target):
        self.control = control
        self.target = target

    def _min(self):
        return min(self.control, self.target)

    def _max(self):
        return max(self.control, self.target)

    @property
    def matrix(self):  # as |0><0|⊗I + |1><1|⊗X
        nqubits = self._max() - self._min() + 1
        ctrl = self.control - self._min()
        targ = self.target - self._min()
        # compute first term
        term0 = [I._matrix] * nqubits
        term0[ctrl] = np.array([[1, 0],
                                [0, 0]])
        term0 = functools.reduce(np.kron, term0[::-1])
        # compute second term
        term1 = [I._matrix] * nqubits
        term1[ctrl] = np.array([[0, 0],
                                [0, 1]])
        term1[targ] = X._matrix
        term1 = functools.reduce(np.kron, term1[::-1])
        return term0 + term1
