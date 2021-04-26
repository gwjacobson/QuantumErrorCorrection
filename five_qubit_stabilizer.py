from qiskit import *
from qiskit.quantum_info import state_fidelity, DensityMatrix, Statevector
import random
from error import *

##

def five_qubit_stabilizer(shots):
    five_array = []

    for error in range(0,10):
        #simulator
        sim = Aer.get_backend('statevector_simulator')

        #inital quantum state
        qr1 = QuantumRegister(4, 'ancilla')
        qr2 = QuantumRegister(5, 'q')
        cr = ClassicalRegister(4, 'c')
        five_qc = QuantumCircuit(qr1, qr2, cr)

        five_fidelity = 0.0

        for i in range(0, shots):
            
            state1 = Statevector(five_qc)

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
            bit = random.randint(4,8) #bit to apply error to
            prob = random.choices([0,1], weights=[(10-error)/10, error/10]) #probability of an error on encoded qubits
            if prob[0] == 1:
                bit_flip(five_qc, bit)
                five_qc.barrier([0,1,2,3,4,5,6,7,8])
            else:
                five_qc.barrier([0,1,2,3,4,5,6,7,8])


            #this is the five qubit stabilizer (4-8) with ancilla measurements (0-3)
            five_qc.h(0)
            five_qc.h(1)
            five_qc.h(2)
            five_qc.h(3)
            five_qc.cz(3, 7)
            five_qc.cx(3, 6)
            five_qc.cx(3, 5)
            five_qc.cz(3, 4)
            five_qc.cz(2, 8)
            five_qc.cz(2, 6)
            five_qc.cx(2, 5)
            five_qc.cx(2, 4)
            five_qc.cx(1, 8)
            five_qc.cz(1, 7)
            five_qc.cz(1, 5)
            five_qc.cx(1, 4)
            five_qc.cx(0, 8)
            five_qc.cx(0, 7)
            five_qc.cz(0, 6)
            five_qc.cz(0, 4)
            five_qc.h(0)
            five_qc.h(1)
            five_qc.h(2)
            five_qc.h(3)
            
            #do error correction
            five_qc.barrier([0,1,2,3,4,5,6,7,8])
            five_qc.cx(6, 8)
            five_qc.h(5)
            five_qc.cx(5, 8)
            five_qc.h(4)
            five_qc.cx(4, 8)
            five_qc.h(7)
            five_qc.cx(6, 7)
            five_qc.h(4)
            five_qc.cx(4, 7)
            five_qc.h(6)
            five_qc.cx(5, 6)
            five_qc.cx(4, 6)
            five_qc.h(5)
            five_qc.h(4)
            five_qc.cx(4, 5)
            five_qc.z(4)
            five_qc.h(4)
            five_qc.z(4)


            #run five_qc
            qobj = assemble(five_qc)
            results = sim.run(qobj).result()
            state2 = Statevector(five_qc) #state after time step to compare fidelity
            fid = state_fidelity(state1,state2)
            five_fidelity += fid
            avg_fid = five_fidelity/shots
        
        five_array.append(avg_fid)

    return five_array