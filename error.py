from qiskit import *
from qiskit.quantum_info.operators import Operator
import random
import numpy as np

## Simulation of a random error. When an error is place with some probability,
## the function will simulation a measurement selection of a Pauli error,
## I,X,Y,Z.

#error will choose a Pauli error each with 25% prob
def error(circuit, qubit):
    error = random.randint(1,4) #25% chance for each selection

    if error == 1:
        circuit.id(qubit) #no error
    elif error == 2:
        circuit.x(qubit) #bit flip error
    elif error == 3:
        circuit.z(qubit) #phase flip error
    else:
        circuit.x(qubit) #combined phase and bit flip
        circuit.z(qubit)


    ## creating arbitrary error with linear combination
    ## e0 I + e1 X + e2 Z + e3 X Z
    #e0 = random.randint(0,1)
    #e1 = random.randint(0,1)
    #e2 = random.randint(0,1)
    #e3 = random.randint(0,1)

    #x = np.matrix([[0,1],[1,0]])
    #z = np.matrix([[1,0],[0,-1]])
    #i = np.matrix([[1,0],[0,1]])

    #error_op = (e1*x)+(e2*z)+(e3*x*z)+(e0*i)
    #eg = Operator(error_op)

    #circuit.unitary(eg, qubit, label='error')
    #circuit.barrier(qubit)

    return
