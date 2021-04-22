from qiskit import *
from qiskit.quantum_info import state_fidelity, DensityMatrix, Statevector
import random
from error import *
import matplotlib.pyplot as plt

##


#simulator
sim = Aer.get_backend('statevector_simulator')

#inital quantum state
five_qc = QuantumCircuit(9,9);

five_fidelity = []
state1 = Statevector(five_qc)

for i in range(1,10):

    #Error on encoded qubits
    for bit in range(4,9):

        prob = random.randint(1,10) #probability of an error on encoded qubits
        if prob == 1:
            #error(five_qc, bit) 
            five_qc.barrier([0,1,2,3,4,5,6,7,8])
        else:
            five_qc.barrier([0,1,2,3,4,5,6,7,8])


    #this is the five qubit stabilizer (4-8) with ancilla measurements (0-3)
    five_qc.h(0)
    five_qc.h(1)
    five_qc.h(2)
    five_qc.h(3)
    five_qc.cx(3, 7)
    five_qc.cz(3, 6)
    five_qc.cz(3, 5)
    five_qc.cx(3, 4)
    five_qc.cx(2, 8)
    five_qc.cz(2, 7)
    five_qc.cz(2, 6)
    five_qc.cx(2, 5)
    five_qc.cz(1, 8)
    five_qc.cz(1, 7)
    five_qc.cx(1, 6)
    five_qc.cx(1, 4)
    five_qc.cz(0, 8)
    five_qc.cx(0, 7)
    five_qc.cx(0, 5)
    five_qc.cz(0, 4)
    five_qc.h(0)
    five_qc.h(1)
    five_qc.h(2)
    five_qc.h(3)
    five_qc.barrier([0,1,2,3,4,5,6,7,8])


    #run circuit

    state2 = DensityMatrix(five_qc)
    fid = state_fidelity(state1, state2)
    five_fidelity.append(fid)


print(five_fidelity)
five_qc.draw(output='mpl')
plt.show()