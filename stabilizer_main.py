from qiskit import *
import matplotlib.pyplot as plt
from control_qubit import *
#from five_qubit_stabilizer import *
#from seven_qubit_stabilizer import *

fidelity_control = control_qubits(5)

plt.plot(range(1,10), fidelity_control, label='Single Qubit')
#plt.plot(range(1,10), five_fidelity, label='Five Qubit Stabilizer')
#plt.plot(range(1,10), seven_fidelity, label='Seven Qunit Stabilizer')
plt.title('Fidelity of Quantum States Exposed to Noise')
plt.xlabel('Time Step')
plt.ylabel('Fidelity')
plt.legend()
plt.show()