from qiskit.primitives import BackendSamplerV2
from qiskit_aer import AerSimulator
from qiskit import transpile




def applysim(circuit,noisemodel=None,method='automatic',optimization_level=1):
    """
    Parameters:
        circuit (QuantumCircuit): The circuit to simulate.
        shots (int): Number of shots to run.
        noise_model (NoiseModel): Optional noise model to include.
        basis_gates (list): Optional list of basis gates to match the noise model.
        optimization_level (int): Transpiler optimization level (0-3).
    """
    
    if method =='automatic':
         qc=circuit.copy()
         qc.measure_all()
         simulator=AerSimulator(method=method,noise_model=noisemodel)
         transpiled_circuit = transpile(qc, backend=simulator,optimization_level=optimization_level)
         return transpiled_circuit,simulator
    else:
         qc=circuit.copy()
         qc.measure_all()
         qc.save_density_matrix()
         simulator=AerSimulator(method=method,noise_model=noisemodel)
         transpiled_circuit = transpile(qc, backend=simulator,optimization_level=optimization_level)
         return transpiled_circuit,simulator
    
        

def simulate_circuit(circuit,noisemodel=None,method='automatic',optimization_level=1):
    if method=='automatic':
        circuit,simulator=applysim(circuit,noisemodel,method,optimization_level)
        sampler=BackendSamplerV2(backend=simulator)
        job=sampler.run([circuit])
        result=job.result()
        return result
    else:
         circuit,simulator=applysim(circuit,noisemodel,method,optimization_level)
         result = simulator.run(circuit, noise_model=noisemodel).result()
         return result





