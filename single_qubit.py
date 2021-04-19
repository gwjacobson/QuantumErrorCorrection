from qiskit import *
from error import error
from qiskit.providers.aer import extensions
from qiskit.quantum_info import state_fidelity, DensityMatrix
import matplotlib.pyplot as plt 
import random

##Single qubit being exposed to random errors from error model.
## 10 time steps are ran, each with 10% prob of error. The fidelity of the
## state is checked after each time step.


sim = Aer.get_backend('qasm_simulator') #simulator

#inital quantum state
q = QuantumCircuit(1,1);



single_fidelity = []

s1 = DensityMatrix(q) #create initial density matrix to compare fidelity

#10 time steps with chance of error
for i in range(1,10):
    prob = random.randint(1, 10) #10% prob

    if prob == 1: #an error is placed from error model
        #error(q, 0)
        q.x(0)
        q.barrier(0)
    else: #nothing happens
        q.barrier(0)

    s2 = DensityMatrix(q) #density matrix after time step to compare fidelity

    fid = state_fidelity(s2, s1) #checking fidelity of each time step
    single_fidelity.append(fid)


print(single_fidelity)
q.draw(output='mpl')
plt.show()