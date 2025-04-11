from qiskit import QuantumCircuit

def bellstategenerator():
    """
    Generates a 2-qubit Bell state circuit.

    Returns:
        QuantumCircuit: Circuit that prepares the Bell state.
    """
    bellqc = QuantumCircuit(2)
    bellqc.h(0)       
    bellqc.cx(0, 1)   
    return bellqc




