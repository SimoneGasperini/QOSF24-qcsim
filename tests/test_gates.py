import numpy as np
from qiskit.circuit.library import IGate, XGate, HGate, CXGate
from qcsim.gates import I, X, H, CNOT


def test_igate():
    qiskit_matrix = IGate().to_matrix()
    qcsim_matrix = I(0).matrix
    assert np.all(qiskit_matrix == qcsim_matrix)


def test_xgate():
    qiskit_matrix = XGate().to_matrix()
    qcsim_matrix = X(0).matrix
    assert np.all(qiskit_matrix == qcsim_matrix)


def test_hgate():
    qiskit_matrix = HGate().to_matrix()
    qcsim_matrix = H(0).matrix
    assert np.all(qiskit_matrix == qcsim_matrix)


def test_cnotgate():
    qiskit_matrix = CXGate().to_matrix()
    qcsim_matrix = CNOT(0, 1).matrix
    assert np.all(qiskit_matrix == qcsim_matrix)
