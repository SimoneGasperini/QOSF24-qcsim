from qcsim import Circuit
from qcsim.gates import X, H, CNOT


def naive_ghz_state_circuit(num_qubits):
    circ = Circuit(num_qubits=num_qubits)
    circ.add(H(0))
    for i in range(0, num_qubits-1):
        circ.add(CNOT(i, i+1))
    return circ


def linear_entanglement_circuit(num_qubits):
    circ = Circuit(num_qubits=num_qubits)
    for i in range(0, num_qubits):
        circ.add(H(i))
    for i in range(0, num_qubits-1):
        circ.add(CNOT(i, i+1))
    for i in range(0, num_qubits):
        circ.add(X(i))
    return circ
