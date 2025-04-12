from qiskit.primitives import BackendSamplerV2
from qiskit_aer import AerSimulator
from qiskit import transpile



def simulatenoise(circuit, simulator):
    sampler=BackendSamplerV2(backend=simulator)
    job=sampler.run([circuit])
    result=job.result()
    return result

def simulateideal(circuit):
    """
    Parameters:
          circuit
    Return:
          Primitiveresult file
    """
    
    simulator=AerSimulator()
    transpiled_circuit=transpile(circuit,simulator)
    sampler=BackendSamplerV2(backend=simulator)
    job=sampler.run([transpiled_circuit])
    result=job.result()
    return result

