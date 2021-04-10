from qiskit import *
import random

##Single qubit being exposed to random errors.
##Loop qubit state 10 times, with 10% chance of
##error after each step.

#inital quantum state
q = QuantumCircuit(1, 1);

for i in range(1,10):
    prob = random.randint(1, 11)

    if prob == 1:
        q.x(0)
        q.barrier(0)
    else:
        q.barrier(0)

print(q)