from qiskit import *
from qiskit.quantum_info.operators import Operator
import random
import numpy as np
from numpy import pi

## Simulation of a random error. When an error is place with some probability,
## the function will simulation a measurement selection of a Pauli error,
## I,X,Y,Z.

#error will choose a Pauli error each with 25% prob
def error(circuit, qubit):

    for i in range(1,4): #get a couple errors to multiple together
        error = random.randint(1,5) #20% chance for each selection

        if error == 1:
            circuit.id(qubit) #no error
        elif error == 2:
            circuit.x(qubit) #bit flip error
        elif error == 3:
            circuit.z(qubit) #phase flip error
        elif error == 4:
            circuit.y(qubit) #combined phase and bit flip, Y gate
        else:
            phase = random.uniform(0.0, 2.0*pi) #random phase error
            circuit.p(phase, qubit)


    return
