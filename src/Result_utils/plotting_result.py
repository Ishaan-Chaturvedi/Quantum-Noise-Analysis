
from qiskit.visualization import plot_histogram,circuit_drawer
import matplotlib.pyplot as plt
import numpy as np


def histogrammaker(result,show=True):
    try:
       counts = getattr(result[0].data, 'meas').get_counts()
    except:
       counts = getattr(result[0].data, 'c').get_counts()
    histdiag=plot_histogram(counts)
    if show:
      plt.show()
    return histdiag


def histcomp(result1,result2,show=True):
   try:
       counts1 = getattr(result1[0].data, 'meas').get_counts()
   except:
       counts1 = getattr(result1[0].data, 'c').get_counts()

   try:
       counts2 = getattr(result2[0].data, 'meas').get_counts()
   except:
       counts2 = getattr(result2[0].data, 'c').get_counts()

   keys = sorted(set(counts1.keys()).union(counts2.keys()))
   values1 = [counts1.get(k, 0) for k in keys]
   values2 = [counts2.get(k, 0) for k in keys]

   fig, ax = plt.subplots(figsize=(10, 6))
   x = np.arange(len(keys))
   width = 0.35
   ax.bar(x - width/2, values1, width, label='Ideal', color='skyblue')
   ax.bar(x + width/2, values2, width, label='Noisy', color='salmon')
   ax.set_ylabel('Probability')
   ax.set_xticks(x)
   ax.set_xticklabels(keys)
   ax.legend()
   plt.tight_layout()
   if show==True:
      plt.show()
   return fig

   
def circuitvis(circuit,show=True):
    diag=circuit_drawer(circuit, output='mpl')
    if show:
       plt.show()
    return diag


    




    

