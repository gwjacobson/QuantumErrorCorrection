from qiskit import *
import matplotlib.pyplot as plt
from single_qubit import *
from five_qubit_stabilizer import *
from seven_qubit_stabilizer import *

plt.plot(range(1,10), single_fidelity, label='Single Qubit')
plt.plot(range(1,10), five_fidelity, label='Five Qubit Stabilizer')
plt.plot(range(1,10), seven_fidelity, label='Seven Qunit Stabilizer')
plt.title('Fidelity of Quantum States Exposed to Noise')
plt.xlabel('Time Step')
plt.ylabel('Fidelity')
plt.legend()
plt.show()