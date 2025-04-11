from qiskit.primitives import BackendSamplerV2

def simulatecircuit(circuit, simulator):
    

    sampler=BackendSamplerV2(backend=simulator)
    job=sampler.run([circuit])
    result=job.result()
    return result