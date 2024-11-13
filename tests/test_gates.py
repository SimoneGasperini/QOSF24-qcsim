import numpy as np
from qiskit.circuit.library import XGate, HGate
from qcsim.gates import X, H


def test_xgate():
    qiskit_matrix = XGate().to_matrix()
    qcsim_matrix = X(0).to_numpy()
    assert np.allclose(qiskit_matrix, qcsim_matrix)


def test_hgate():
    qiskit_matrix = HGate().to_matrix()
    qcsim_matrix = H(0).to_numpy()
    assert np.allclose(qiskit_matrix, qcsim_matrix)
