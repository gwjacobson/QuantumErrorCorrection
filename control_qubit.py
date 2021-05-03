from qiskit import *
from error import *
from qiskit.providers.aer import extensions
from qiskit.quantum_info import state_fidelity, DensityMatrix, Statevector
import matplotlib.pyplot as plt 
import random
from qiskit.visualization import plot_histogram

##Single qubit being exposed to random errors from error model.
## 10 time steps are ran, each with 10% prob of error. The fidelity of the
## state is checked after each time step.

#define qubits to test, the probability of finding an error, and number of shots
def control_qubits(qubits, shots): 
    
    fid_array = []

    for error in range(0,10):
        
        sim = Aer.get_backend('statevector_simulator') #simulator

        #inital quantum state
        qr = QuantumRegister(qubits, 'q')
        cr = ClassicalRegister(qubits, 'c')
        qc = QuantumCircuit(qr, cr)

        #array of state fidelities from each run
        fidelity = 0.0
        avg_fid = 0.0

        #create initial state to compare fidelity
        qobj1 = assemble(qc)
        state1 = sim.run(qobj1).result().get_statevector()

        for i in range(0, shots):
            #qobj1 = assemble(qc)
            #state1 = sim.run(qobj1).result().get_statevector()
                    

            prob = random.choices([0,1], weights=[(10-error)/10, error/10], k=1) #variable probability of error
            bit = random.randint(0, qubits-1) #qubit to apply error to

            if prob[0] == 1:
                phase_flip(qc, bit)
                qc.barrier(qr)
            else:
                qc.barrier(qr)
            

            #run the circuit
            qobj2 = assemble(qc)
            results = sim.run(qobj2).result()
            state2 = results.get_statevector() #state after time step to compare fidelity
            fid = state_fidelity(state1,state2)
            fidelity += fid
            avg_fid = fidelity/shots
        
        fid_array.append(avg_fid)

    return fid_array