import numpy as np
from hypothesis import given, strategies
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qcsim import Simulator
from qcsim.misc import naive_ghz_state_circuit as GHZ_circuit
from qcsim.misc import linear_entanglement_circuit as LE_circuit


@given(num_qubits=strategies.integers(min_value=2, max_value=8),
       method=strategies.sampled_from(['matrix-mul', 'tensor-mul']))
def test_GHZ_circuit(num_qubits, method):
    qiskit_circ = QuantumCircuit(num_qubits)
    qiskit_circ.h(0)
    for i in range(0, num_qubits-1):
        qiskit_circ.cx(i, i+1)
    qiskit_statevec = Statevector(qiskit_circ).data
    qcsim_circ = GHZ_circuit(num_qubits)
    sim = Simulator(method=method)
    sim.run(circuit=qcsim_circ)
    qcsim_statevec = sim.get_statevector()
    assert np.all(qiskit_statevec == qcsim_statevec)


@given(num_qubits=strategies.integers(min_value=2, max_value=8),
       method=strategies.sampled_from(['matrix-mul', 'tensor-mul']))
def test_LE_circuit(num_qubits, method):
    qiskit_circ = QuantumCircuit(num_qubits)
    for i in range(0, num_qubits):
        qiskit_circ.h(i)
    for i in range(0, num_qubits-1):
        qiskit_circ.cx(i, i+1)
    for i in range(0, num_qubits):
        qiskit_circ.x(i)
    qiskit_statevec = Statevector(qiskit_circ).data
    qcsim_circ = LE_circuit(num_qubits)
    sim = Simulator(method=method)
    sim.run(circuit=qcsim_circ)
    qcsim_statevec = sim.get_statevector()
    assert np.all(qiskit_statevec == qcsim_statevec)
