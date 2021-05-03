from qiskit import *
import matplotlib.pyplot as plt
from control_qubit import *
from five_qubit_stabilizer import *
from seven_qubit_stabilizer import *

def test(shots):
    control1 = control_qubits(1, shots)
    control3 = control_qubits(3, shots)
    control5 = control_qubits(5, shots)
    fivestab = five_qubit_stabilizer(shots)
    sevenstab = seven_qubit_stabilizer(shots)

    plt.plot(range(0,100,10), control1, label='Single Qubit')
    plt.plot(range(0,100,10), control3, label='Five Qubits')
    plt.plot(range(0,100,10), control5, label='Seven Qubits')
    plt.plot(range(0,100,10), fivestab, label='Five Qubit Stabilizer')
    plt.plot(range(0,100,10), sevenstab, label='Seven Qubit Stabilizer')
    
    plt.title('Fidelity of Quantum States Exposed to Arbitrary Errors')
    plt.xlabel('Probability of Error %')
    plt.ylabel('Fidelity')
    plt.legend()
    plt.savefig('arbitrary_plot.png')
    plt.show()

    return

test(100)