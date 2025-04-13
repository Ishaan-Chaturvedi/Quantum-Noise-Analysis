from qiskit.quantum_info import state_fidelity

def interpret_result(result,key='meas'):
    #dist = result.counts[0]
    print("Measurement outcomes (Probability distribution)->")
    try:
       counts = getattr(result[0].data, 'meas').get_counts()
    except:
       counts = getattr(result[0].data, 'c').get_counts()
    print(counts)

    
    #for outcome, prob in dist.items():
      #print(f"{outcome}:{prob:.4f}")
"""
def compare_result(ideal_result,noisy_result):
    ideal_dist=ideal_result.quasi_dists(0)
    noisy_dist=noisy_result.quasi_dists(0)

    print("Measurement outcomes 1 (Probability distribution)->")
    for outcome, prob in ideal_dist.items():
        print(f"{outcome}:{prob:.4f}")

    print("Measurement outcomes 1 (Probability distribution)->")
    for outcome, prob in noisy_dist.items():
        print(f"{outcome}:{prob:.4f}")
"""


