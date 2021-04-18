from qiskit import *
import matplotlib.pyplot as plt
from single_qubit import *
from five_qubit_stabilizer import *
from seven_qubit_stabilizer import *

plt.plot(range(1,50), single_fidelity)
plt.title('Fidelity of Quantum States Exposed to Noise')
plt.xlabel('Time Step')
plt.ylabel('Fidelity')
plt.show()