from qiskit import *
from qiskit.quantum_info import state_fidelity, DensityMatrix
import random
from error import error
import matplotlib.pyplot as plt

##

sim = Aer.get_backend('qasm_simulator') #simulator

#inital quantum state
q = QuantumCircuit(9,9);

five_fidelity = []
s1 = DensityMatrix(q)

for i in range(1,10):

    #probability of error on q4
    for bit in range(5,9):

        p = random.randint(1,10)
        if p == 1:
            error(q, bit)
            q.barrier([0,1,2,3,4,5,6,7,8])
        else:
            q.barrier([0,1,2,3,4,5,6,7,8])

    q.h(0)
    q.h(1)
    q.h(2)
    q.h(3)
    q.cx(3, 7)
    q.cz(3, 6)
    q.cz(3, 5)
    q.cx(3, 4)
    q.cx(2, 8)
    q.cz(2, 7)
    q.cz(2, 6)
    q.cx(2, 5)
    q.cz(1, 8)
    q.cz(1, 7)
    q.cx(1, 6)
    q.cx(1, 4)
    q.cz(0, 8)
    q.cx(0, 7)
    q.cx(0, 5)
    q.cz(0, 4)
    q.h(0)
    q.h(1)
    q.h(2)
    q.h(3)
    q.barrier([0,1,2,3,4,5,6,7,8])

    s2 = DensityMatrix(q)
    fid = state_fidelity(s1, s2)
    five_fidelity.append(fid)


print(five_fidelity)
q.draw(output='mpl')
plt.show()