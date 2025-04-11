
from qiskit_aer.noise import NoiseModel, depolarizing_error, amplitude_damping_error


def depolarizing_noise(p1=0.05,p2=0.05):
    
      noisemodel=NoiseModel()
      noisemodel.add_all_qubit_quantum_error(depolarizing_error(p1,1),['h'])
      noisemodel.add_all_qubit_quantum_error(depolarizing_error(p2,2),['cx'])
      return noisemodel

    
