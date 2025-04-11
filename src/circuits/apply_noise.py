from qiskit_aer import AerSimulator
from qiskit import transpile


def applynoise(circuit,noisemodel, optimization_level=1):
    """
    Parameters:
        circuit (QuantumCircuit): The circuit to simulate.
        shots (int): Number of shots to run.
        noise_model (NoiseModel): Optional noise model to include.
        basis_gates (list): Optional list of basis gates to match the noise model.
        optimization_level (int): Transpiler optimization level (0-3).
    """
    simulator=AerSimulator(noise_model=noisemodel)
    transpiled_circuit = transpile(circuit, backend=simulator,optimization_level=optimization_level)
    return transpiled_circuit,simulator
