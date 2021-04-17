from qiskit import *
from error import error
from qiskit.providers.aer import extensions
import random

##Single qubit being exposed to random errors from noise model.

sim = Aer.get_backend('qasm_simulator')

#inital quantum state
q = QuantumCircuit(1,1);

q.h(0)

s1 = qiskit.quantum_info.DensityMatrix(q)


for i in range(1,10):
    prob = random.randint(1, 15)

    if prob == 1:
        error(q, 0)
        q.barrier(0)
    else:
        q.barrier(0)

    s2 = qiskit.quantum_info.DensityMatrix(q)

    print(qiskit.quantum_info.state_fidelity(s1, s2))

print(q)