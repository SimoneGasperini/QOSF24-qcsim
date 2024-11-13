import sympy
import numpy


class X:
    num_qubits = 1
    matrix = sympy.Array([[0, 1],
                          [1, 0]])

    def __init__(self, qubit):
        self.qubit = qubit

    def to_numpy(self):
        return numpy.array(self.matrix, dtype=complex)


class H:
    num_qubits = 1
    matrix = 1/sympy.sqrt(2) * sympy.Array([[1, 1],
                                            [1, -1]])

    def __init__(self, qubit):
        self.qubit = qubit

    def to_numpy(self):
        return numpy.array(self.matrix, dtype=complex)


class CNOT:
    num_qubits = 2
    matrix = sympy.Array([[1, 0, 0, 0],
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

    def to_numpy(self):
        return numpy.array(self.matrix, dtype=complex)
