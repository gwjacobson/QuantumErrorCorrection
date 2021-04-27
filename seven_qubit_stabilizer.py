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
        qr1 = QuantumRegister(3, 'ancilla')
        qr2 = QuantumRegister(7, 'q')
        cr = ClassicalRegister(3, 'c')
        seven_qc = QuantumCircuit(qr2, qr1, cr)

        seven_fidelity = 0.0
        avg_fid = 0.0

        for i in range(0, shots):
            
            qobj = assemble(seven_qc)
            state1 = sim.run(qobj).result().get_statevector()

            #Error on encoded qubits
            bit = random.randint(0,6)#bit to apply error to
            prob = random.choices([0,1], weights=[(10-error)/10, error/10]) #probability of an error on encoded qubits
            if prob[0] == 1:
                arbitrary_error(seven_qc, bit)
                seven_qc.barrier([0,1,2,3,4,5,6,7,8,9])
            else:
                seven_qc.barrier([0,1,2,3,4,5,6,7,8,9])


            #this is the seven qubit stabilizer (0-6) for phase flips with ancilla measurements (7-9)
            seven_qc.h(7)
            seven_qc.h(8)
            seven_qc.h(9)
            seven_qc.cx(0, 7)
            seven_qc.cx(1, 7)
            seven_qc.cx(2, 7)
            seven_qc.cx(3, 7)
            seven_qc.cx(0, 8)
            seven_qc.cx(2, 8)
            seven_qc.cx(4, 8)
            seven_qc.cx(6, 8)
            seven_qc.cx(0, 9)
            seven_qc.cx(1, 9)
            seven_qc.cx(4, 9)
            seven_qc.cx(5, 9)
            seven_qc.h(7)
            seven_qc.h(8)
            seven_qc.h(9)
            seven_qc.measure(7,0)
            seven_qc.measure(8,1)
            seven_qc.measure(9,2)

            #check ancilla measurements
            qobj = assemble(seven_qc)
            results = sim.run(qobj).result()
            parity_pf = results.get_statevector()
            
            #do error correction on phase flips
            seven_qc.x(5).c_if(cr,1)
            seven_qc.x(6).c_if(cr,2)
            seven_qc.x(4).c_if(cr,3)
            seven_qc.x(3).c_if(cr,4)
            seven_qc.x(1).c_if(cr,5)
            seven_qc.x(2).c_if(cr,6)
            seven_qc.x(0).c_if(cr,7)

            #stabilizers for bit flip
            seven_qc.initialize([1,0], 7)
            seven_qc.initialize([1,0], 8)
            seven_qc.initialize([1,0], 9)

            seven_qc.h(7)
            seven_qc.h(8)
            seven_qc.h(9)
            seven_qc.cz(0, 7)
            seven_qc.cz(1, 7)
            seven_qc.cz(2, 7)
            seven_qc.cz(3, 7)
            seven_qc.cz(0, 8)
            seven_qc.cz(2, 8)
            seven_qc.cz(4, 8)
            seven_qc.cz(6, 8)
            seven_qc.cz(0, 9)
            seven_qc.cz(1, 9)
            seven_qc.cz(4, 9)
            seven_qc.cz(5, 9)
            seven_qc.h(7)
            seven_qc.h(8)
            seven_qc.h(9)
            seven_qc.measure(7,0)
            seven_qc.measure(8,1)
            seven_qc.measure(9,2)

            #check ancilla measurements
            qobj = assemble(seven_qc)
            results = sim.run(qobj).result()
            parity_bf = results.get_statevector()

            #do error correction
            seven_qc.z(5).c_if(cr,1)
            seven_qc.z(6).c_if(cr,2)
            seven_qc.z(4).c_if(cr,3)
            seven_qc.z(3).c_if(cr,4)
            seven_qc.z(1).c_if(cr,5)
            seven_qc.z(2).c_if(cr,6)
            seven_qc.z(0).c_if(cr,7)

            #run seven_qc
            qobj = assemble(seven_qc)
            state2 = sim.run(qobj).result().get_statevector() #state after time step to compare fidelity
            fid = state_fidelity(state1,state2)
            seven_fidelity += fid
            avg_fid = seven_fidelity/shots
        
        seven_array.append(avg_fid)

    return seven_array