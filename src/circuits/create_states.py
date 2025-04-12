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
    bellqc.measure_all()
    return bellqc

def ghzstategenerator(n=3):

    """
    parameter:
         n: no of qubits
    returns:
         QuantumCircuit: prepares ghz state
    generates a ghz state for n qubits
    """
    ghzqc=QuantumCircuit(n)
    ghzqc.h(0)
    for i in range(n-1):
        ghzqc.cx(i,i+1)
    ghzqc.measure_all()
    return ghzqc
    
def teleportationcircuit():
    """
    create quantum teleportation circuit
    returns:
        QuantumCircuit: qc teleportation circuit
    """
    teleqc=QuantumCircuit(3,3)
    teleqc.h(1)
    teleqc.cx(1,2)
    #created bell state for the last 2 qubits
    teleqc.cx(0,1)
    teleqc.h(0)
    #now for measurement part
    teleqc.measure([0,1],[0,1])
    with teleqc.if_test((0,True)):
        teleqc.x(2)
    with teleqc.if_test((1,True)):
        teleqc.z(2)
    #information transfered
    teleqc.measure(2,2)
    return teleqc






