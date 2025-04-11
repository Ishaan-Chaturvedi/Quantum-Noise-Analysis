from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error, amplitude_damping_error
from qiskit import transpile

def depolarizing_noise(p1=0.05,p2=0.05):
    
      noisemodel=NoiseModel()
      noisemodel.add_all_qubit_quantum_error(depolarizing_error(p1,1),['h'])
      noisemodel.add_all_qubit_quantum_error(depolarizing_error(p2,2),['cx'])
      return noisemodel

    
def applynoise(circuit,noisemodel):
    
    simulator=AerSimulator(noise_model=noisemodel)
    transpiled_circuit = transpile(circuit, backend=simulator)
    return transpiled_circuit,simulator
