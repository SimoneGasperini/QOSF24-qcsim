# qcsim: "Statevector simulation of quantum circuits"
### [QOSF](https://qosf.org/) Mentorship Program 2024, screening task 1

To install the software directly from the source code hosted in the GitHub repository, you can do:
```bash
pip install git+https://github.com/SimoneGasperini/QOSF24-qcsim.git
```

To test the software implementing the statevector simulator for quantum circuits, you can do:
```bash
pytest -v tests
```

In the [notebooks](https://github.com/SimoneGasperini/QOSF24-qcsim/tree/master/notebooks) directory you find some Jupyter notebooks with a few tests and examples required to complete the task:
- the first notebook is showing the plot comparing the runtime of the quantum circuit simualtion (versus the number of qubits) using the two different approaches (naive matrix multiplication, advanced tensor multiplication);
- the second notebook is showing how to sample the final statevector to get the output bitstrings distribution and how to compute the exact expectation value of a given observable.
