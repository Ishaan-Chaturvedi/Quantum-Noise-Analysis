import numpy as np
from scipy.linalg import sqrtm
from qiskit.quantum_info import state_fidelity, entropy

def interpret_result(result,prob=False,key='meas',show=True):
    
    try:
       counts = getattr(result[0].data, 'meas').get_counts()
    except:
       counts = getattr(result[0].data, 'c').get_counts()

    if prob:

      total=sum(counts.values())
      prob={k: v/total for k,v in counts.items()}
      if show:
          print("Measurement outcomes (Probability)->")
          print(prob)

      return prob
    
    else:
       
       if show:
          print("Measurement outcomes (Counts)->")
          print(counts)

       return counts

    
    #for outcome, prob in dist.items():
      #print(f"{outcome}:{prob:.4f}")

def measurement_fidelity(result1,result2):
    prob1=interpret_result(result1,prob=True,show=False)
    prob2=interpret_result(result2,prob=True,show=False) 
    #need to normalize for prob
    
    all_keys = set(prob1.keys()).union(prob2.keys())
    fidelity = sum(np.sqrt(prob1.get(k,0) * prob2.get(k,0)) for k in all_keys) ** 2
    return fidelity

def operator_fidelity(result1,result2):
    rho = result1.data(0)['density_matrix']
    sigma = result2.data(0)['density_matrix']
    # Step 6: Compute quantum fidelity
    fidelity = state_fidelity(rho, sigma)
    return fidelity

def measurement_trace(result1,result2):
    prob1=interpret_result(result1,prob=True,show=False)
    prob2=interpret_result(result2,prob=True,show=False) 
    all_keys = set(prob1.keys()).union(prob2.keys())
    trace = 0.5 * sum(abs(prob1.get(k, 0) - prob2.get(k, 0)) for k in all_keys)
    return trace

def operator_trace(result1,result2):
    rho = result1.data(0)['density_matrix']
    sigma = result2.data(0)['density_matrix']
    delta = rho.data - sigma.data
    sqrt_delta_dagger_delta = sqrtm(delta.conj().T @ delta)
    trace_norm = np.trace(sqrt_delta_dagger_delta).real
    return 0.5 * trace_norm

def information_gain(result1, result2):
     rho = result1.data(0)['density_matrix']
     sigma = result2.data(0)['density_matrix']
     info_gain=entropy(sigma)-entropy(rho)
     return info_gain

def shannon_information_gain(result1,result2):
    prob1=interpret_result(result1,prob=True,show=False)
    prob2=interpret_result(result2,prob=True,show=False) 
    entropy1= -sum(p1 * np.log2(p1) for p1 in prob1.values() if p1 > 0)
    entropy2= -sum(p2 * np.log2(p2) for p2 in prob2.values() if p2 > 0)
    info_gain=entropy2-entropy1
    return info_gain



def measresult(result1,result2,show=True):
    str="The Measures of difference between ideal circuit and noisy circuit on the basis of measurement are-\n\n"
    str+=f"1. Fidelity(between measurement probability distribution) is {measurement_fidelity(result1,result2):4f}\n"
    str+=f"2. Trace Distance(probability distribution)={measurement_trace(result1,result2):.4f}\n"
    str+=f"3. Information gain(change in shannon entropy from ideal to noisy circuit) is{shannon_information_gain(result1,result2):.4f}\n\n\n"
    if show:
        print(str)
    else:
        return str

def operesult(result1,result2,show=True):
    str="The Measures of difference between ideal circuit and noisy circuit (Density_matrix) are-\n\n"
    str+=f"1. Fidelity(Density_Matrix) is {operator_fidelity(result1,result2):.4f}\n"
    str+=f"2. Trace Distance(Density_matrix) is {operator_trace(result1,result2):.4f}\n"
    str+=f"3. Information gain(change in von neumann entropy from ideal to noisy circuit) is {information_gain(result1,result2):.4f}\n\n"
    if show:
        print(str)
    else:
        return str



