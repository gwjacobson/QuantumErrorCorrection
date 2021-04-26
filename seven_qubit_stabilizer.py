from qiskit import *
from qiskit.quantum_info import state_fidelity, DensityMatrix, Statevector
import random
from error import *

##

def seven_qubit_stabilizer(shots):
    seven_array = []

    for error in range(0,10):
        #simulator
        sim = Aer.get_backend('statevector_simulator')

        #inital quantum state
        qr1 = QuantumRegister(6, 'ancilla')
        qr2 = QuantumRegister(7, 'q')
        cr = ClassicalRegister(6, 'c')
        seven_qc = QuantumCircuit(qr1, qr2, cr)

        seven_fidelity = 0.0

        for i in range(0, shots):
            
            state1 = Statevector(seven_qc)

            #Error on encoded qubits
            bit = random.randint(6,12) #bit to apply error to
            prob = random.choices([0,1], weights=[(10-error)/10, error/10]) #probability of an error on encoded qubits
            if prob[0] == 1:
                bit_flip(seven_qc, bit)
                seven_qc.barrier([0,1,2,3,4,5,6,7,8,9,10,11,12])
            else:
                seven_qc.barrier([0,1,2,3,4,5,6,7,8,9,10,11,12])


            #this is the seven qubit stabilizer (6-12) with ancilla measurements (0-5)
            seven_qc.h(0)
            seven_qc.h(1)
            seven_qc.h(2)
            seven_qc.h(3)
            seven_qc.cz(3, 7)
            seven_qc.cx(3, 6)
            seven_qc.cx(3, 5)
            seven_qc.cz(3, 4)
            seven_qc.cz(2, 8)
            seven_qc.cz(2, 6)
            seven_qc.cx(2, 5)
            seven_qc.cx(2, 4)
            seven_qc.cx(1, 8)
            seven_qc.cz(1, 7)
            seven_qc.cz(1, 5)
            seven_qc.cx(1, 4)
            seven_qc.cx(0, 8)
            seven_qc.cx(0, 7)
            seven_qc.cz(0, 6)
            seven_qc.cz(0, 4)
            seven_qc.h(0)
            seven_qc.h(1)
            seven_qc.h(2)
            seven_qc.h(3)
            
            #do error correction


            #run seven_qc
            qobj = assemble(seven_qc)
            results = sim.run(qobj).result()
            state2 = Statevector(seven_qc) #state after time step to compare fidelity
            fid = state_fidelity(state1,state2)
            seven_fidelity += fid
            avg_fid = seven_fidelity/shots
        
        seven_array.append(avg_fid)

    return seven_array