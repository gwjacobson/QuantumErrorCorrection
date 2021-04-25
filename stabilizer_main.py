from qiskit import *
import matplotlib.pyplot as plt
from control_qubit import *
from five_qubit_stabilizer import *
#from seven_qubit_stabilizer import *

def test(shots):
    control1 = control_qubits(1, shots)
    control3 = control_qubits(3, shots)
    control5 = control_qubits(5, shots)
    fivestab = five_qubit_stabilizer(shots)

    plt.plot(range(0,100,10), control1, label='Single Qubit')
    plt.plot(range(0,100,10), control3, label='Five Qubits')
    plt.plot(range(0,100,10), control5, label='Seven Qubits')
    
    plt.title('Fidelity of Quantum States Exposed to Noise')
    plt.xlabel('Probability of Error %')
    plt.ylabel('Fidelity')
    plt.legend()
    plt.show()

    return

test(50)