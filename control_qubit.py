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

def control_qubits(qubits): 
    sim = Aer.get_backend('statevector_simulator') #simulator

    #inital quantum state
    qr = QuantumRegister(qubits, 'q')
    cr = ClassicalRegister(qubits, 'c')
    qc = QuantumCircuit(qr, cr)

    #array of state fidelities from each run
    fidelity = []

    #create initial state to compare fidelity
    state1 = Statevector(qc)

    for i in range(1,10):
        prob = random.randint(1,10) #10% probability of error
        bit = random.randint(0, qubits) #qubit to apply error to

        if prob == 1:
            arbitrary_error(qc, bit)
            qc.barrier(qr)
        else:
            qc.barrier(qr)

        #run the circuit
        qobj = assemble(qc)
        results = sim.run(qobj).result()
        state2 = results.get_statevector() #state after time step to compare fidelity
        fid = state_fidelity(state1,state2)
        fidelity.append(fid)



    print(fidelity)
    qc.draw(output='mpl')
    plt.show()
    return fidelity