import numpy as np

def interpret_result(result,key='meas',show=True):
    #dist = result.counts[0]
    
    try:
       counts = getattr(result[0].data, 'meas').get_counts()
    except:
       counts = getattr(result[0].data, 'c').get_counts()
    if show:
       print("Measurement outcomes (Probability distribution)->")
       print(counts)
    return counts

    
    #for outcome, prob in dist.items():
      #print(f"{outcome}:{prob:.4f}")

def measurement_fidelity(result1,result2):
    counts1=interpret_result(result1,show=False)
    counts2=interpret_result(result2,show=False) 
    #need to normalize for prob
    total1=sum(counts1.values())
    total2=sum(counts2.values())
    prob1={k: v/total1 for k,v in counts1.items()}
    prob2={k: v/total2 for k,v in counts2.items()}
    all_keys = set(prob1.keys()).union(prob2.keys())
    fidelity = sum(np.sqrt(prob1.get(k,0) * prob2.get(k,0)) for k in all_keys) ** 2
    return fidelity
   

