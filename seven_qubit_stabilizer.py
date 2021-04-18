from qiskit import *
from qiskit.quantum_info import state_fidelity, DensityMatrix
import random
from error import error
import matplotlib.pyplot as plt

##

sim = Aer.get_backend('qasm_simulator') #simulator

#inital quantum state
q = QuantumCircuit(9,9);

seven_fidelity = []
s1 = DensityMatrix(q)

for i in range(1,10):

    #probability of error on q4
    for bit in range(6,13):

        p = random.randint(1,10)
        if p == 1:
            error(q, bit)
            q.barrier([0,1,2,3,4,5,6,7,8,9,10,11,12])
        else:
            q.barrier([0,1,2,3,4,5,6,7,8,9,10,11,12])

    q.h(0)
    q.h(1)
    q.h(2)
    q.h(3)
    q.h(4)
    q.h(5)
    q.cx(5, 1)
    q.cx(5, 1)
    q.cx(5, 1)
    q.cx(5, 9)
    q.cx(4, 1)
    q.cx(4, 1)
    q.cx(4, 8)
    q.cx(4, 7)
    q.cx(3, 1)
    q.cx(3, 1)
    q.cx(3, 8)
    q.cx(3, 6)
    q.cz(2, 1)
    q.cz(2, 1)
    q.cz(2, 1)
    q.cz(2, 9)
    q.cz(1, 1)
    q.cz(1, 1)
    q.cz(1, 8)
    q.cz(1, 7)
    q.cz(0, 1)
    q.cz(0, 1)
    q.cz(0, 8)
    q.cz(0, 6)
    q.h(0)
    q.h(1)
    q.h(2)
    q.h(3)
    q.h(4)
    q.h(5)
    q.barrier([0,1,2,3,4,5,6,7,8,9,10,11,12])

    s2 = DensityMatrix(q)
    fid = state_fidelity(s1, s2)
    five_fidelity.append(fid)


print(seven_fidelity)
q.draw(output='mpl')
plt.show()