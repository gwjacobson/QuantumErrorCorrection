from qiskit import *
import random

## Simulation of a random error. When an error is place with some probability,
## the function will simulation a measurement selection of a Pauli error,
## I,X,Y,Z.

#error will choose a Pauli error each with 25% prob
def error(circuit, qubit):
    error = random.randint(1,4) #25% chance for each selection

    if error == 1:
        circuit.id(0) #no error
    elif error == 2:
        circuit.x(qubit) #bit flip error
    elif error == 3:
        circuit.z(qubit) #phase flip error
    else:
        circuit.x(qubit) #combined phase and bit flip
        circuit.z(qubit)

    return
