from qiskit import *
from qiskit.quantum_info import state_fidelity, DensityMatrix, Statevector
import random
from error import *
import matplotlib.pyplot as plt

##

def five_qubit_stabilizer(shots):
    five_array = []

    for error in range(0,10):
        #simulator
        sim = Aer.get_backend('statevector_simulator')

        #inital quantum state
        five_qc = QuantumCircuit(9,9);

        five_fidelity = 0.0
        state1 = Statevector(five_qc)

        for i in range(0, shots):

            #encoding of five qubits
            five_qc.z(4)
            five_qc.h(4)
            five_qc.z(4)
            five_qc.cx(4, 5)
            five_qc.h(4)
            five_qc.h(5)
            five_qc.cx(4, 6)
            five_qc.cx(5, 6)
            five_qc.h(6)
            five_qc.cx(4, 7)
            five_qc.h(4)
            five_qc.cx(6, 7)
            five_qc.h(7)
            five_qc.cx(4, 8)
            five_qc.h(4)
            five_qc.cx(5, 8)
            five_qc.h(5)
            five_qc.cx(6, 8)
            five_qc.barrier([0,1,2,3,4,5,6,7,8])


            #Error on encoded qubits
            bit = random.randint(4,9) #bit to apply error to
            prob = random.choices([0,1], weights=[(10-error)/10, error/10]) #probability of an error on encoded qubits
            if prob[0] == 1:
                arbitrary_error(five_qc, bit)
                five_qc.barrier([0,1,2,3,4,5,6,7,8])
            else:
                five_qc.barrier([0,1,2,3,4,5,6,7,8])


            #this is the five qubit stabilizer (4-8) with ancilla measurements (0-3)




            #run five_qc
            qobj = assemble(five_qc)
            results = sim.run(qobj).result()
            state2 = results.get_statevector() #state after time step to compare fidelity
            fid = state_fidelity(state1,state2)
            fidelity += fid
            avg_fid = fidelity/shots
        
        five_array.append(avg_fid)

    return five_array