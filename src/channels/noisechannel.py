
from qiskit_aer.noise import NoiseModel, depolarizing_error, amplitude_damping_error, phase_damping_error, pauli_error


def depolarizing_noise(p1=0.05,p2=0.05):
    
      noisemodel=NoiseModel()
      noisemodel.add_all_qubit_quantum_error(depolarizing_error(p1,1),['h'])
      noisemodel.add_all_qubit_quantum_error(depolarizing_error(p2,2),['cx'])
      return noisemodel


def amplitude_damping(p=0.1,gate_list=['x','h']):
    """
    parameters:
            p: damping probability
    returns:
            noisemodel: with amp damp
    """ 

    noisemodel=NoiseModel()
    error=amplitude_damping_error(p)
    noisemodel.add_all_qubit_quantum_error(error, gate_list)
    return noisemodel

def phase_damping(p=0.1,gate_list=['x','h']):
     """
     parameters:
            p: damping probability
     returns:
            noisemodel: with phase damp
     """
     noisemodel=NoiseModel()
     error=phase_damping_error(p)
     noisemodel.add_all_qubit_quantum_error(error,gate_list)
     return noisemodel

def bit_flip(p=0.1,gate_list=['x','h']):
     """
     parameters:   
        p:flip probability
     returns:
        noisemodel: with bit flip
     """
     noisemodel=NoiseModel()
     error=pauli_error([('X',p),('I',1-p)])
     noisemodel.add_all_qubit_quantum_error(error, gate_list)
     return noisemodel



    
