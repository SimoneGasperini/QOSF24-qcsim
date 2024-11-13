class Circuit:

    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self._data = []

    def add(self, gate):
        self._data.append(gate)
