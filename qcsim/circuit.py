from qcsim.gates import I


class Circuit:

    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self._data = []
        self._init_new_layer()

    def _init_new_layer(self):
        new_layer = [I(i) for i in range(self.num_qubits)]
        self._data.append(new_layer)

    def add(self, gate):
        curr_layer = self._data[-1]
        if gate.num_qubits == 1:
            q = gate.qubit
            if not isinstance(curr_layer[q], I):
                self._init_new_layer()
            self._data[-1][q] = gate
        elif gate.num_qubits == 2:
            q1 = gate._min()
            q2 = gate._max()
            if any(not isinstance(curr_layer[i], I) for i in range(q1, q2+1)):
                self._init_new_layer()
            self._data[-1][q1] = gate
            for i in range(q1+1, q2+1):
                self._data[-1][i] = None
        else:
            error_message = 'Gates with more that 2 qubits are not implemented!'
            raise NotImplementedError(error_message)
