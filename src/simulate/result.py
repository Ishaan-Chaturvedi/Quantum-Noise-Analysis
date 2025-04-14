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
     info_gain=-entropy(sigma)+entropy(rho)
     return info_gain

   



