from qiskit import *
from error import error
from qiskit.providers.aer import extensions
from qiskit.quantum_info import state_fidelity, DensityMatrix, Statevector
import matplotlib.pyplot as plt 
import random
from qiskit.visualization import plot_histogram

##Single qubit being exposed to random errors from error model.
## 10 time steps are ran, each with 10% prob of error. The fidelity of the
## state is checked after each time step.


sim = Aer.get_backend('statevector_simulator') #simulator

#inital quantum state
single_qc = QuantumCircuit(1)

#array of state fidelities from each run
single_fidelity = []

#create initial state to compare fidelity
state1 = Statevector(single_qc)

for i in range(1,10):
    prob = random.randint(1,10) #10% probability of error

    if prob == 1:
        error(single_qc, 0)
        single_qc.barrier(0)
    else:
        single_qc.barrier(0)

    #run the circuit
    qobj = assemble(single_qc)
    results = sim.run(qobj).result()
    state2 = results.get_statevector() #state after time step to compare fidelity
    fid = state_fidelity(state1,state2)
    single_fidelity.append(fid)



print(single_fidelity)
single_qc.draw(output='mpl')
plt.show()