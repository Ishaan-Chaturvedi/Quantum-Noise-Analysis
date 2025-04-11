from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error, amplitude_damping_error
from qiskit import transpile
from qiskit import QuantumCircuit
from qiskit.primitives import BackendSamplerV2

qc=QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)

def applynoise(circuit):
    noisemodel=NoiseModel()
    
    noisemodel.add_all_qubit_quantum_error(depolarizing_error(0.05,1),['h'])
    noisemodel.add_all_qubit_quantum_error(depolarizing_error(0.05,2),['cx'])
    simulator=AerSimulator(noise_model=noisemodel)
    transpiled_circuit = transpile(circuit, backend=simulator)
    return transpiled_circuit,simulator
circ,sim=applynoise(qc)

circ.measure_all()
sampler = BackendSamplerV2(backend=sim)
job = sampler.run([circ])
result = job.result()
print(result[0])
