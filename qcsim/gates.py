import functools
import numpy as np


class I:
    matrix = np.array([[1, 0],
                       [0, 1]])

    def __init__(self, qubit):
        self.qubit = qubit


class X:
    matrix = np.array([[0, 1],
                       [1, 0]])

    def __init__(self, qubit):
        self.qubit = qubit


class H:
    matrix = 1/np.sqrt(2) * np.array([[1, 1],
                                      [1, -1]])

    def __init__(self, qubit):
        self.qubit = qubit


class CNOT:

    def __init__(self, control, target):
        self.control = control
        self.target = target

    @property
    def matrix(self):  # as |0><0|⊗I + |1><1|⊗X
        nqubits = abs(self.control - self.target) + 1
        shift = min(self.control, self.target)
        ctrl = self.control - shift
        targ = self.target - shift
        # compute first term
        term0 = [I.matrix] * nqubits
        term0[ctrl] = np.array([[1, 0],
                                [0, 0]])
        term0 = functools.reduce(np.kron, term0[::-1])
        # compute second term
        term1 = [I.matrix] * nqubits
        term1[ctrl] = np.array([[0, 0],
                                [0, 1]])
        term1[targ] = X.matrix
        term1 = functools.reduce(np.kron, term1[::-1])
        return term0 + term1
