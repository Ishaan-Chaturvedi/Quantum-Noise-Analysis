from matplotlib.backends.backend_pdf import PdfPages
from qiskit.visualization import plot_histogram,circuit_drawer
import matplotlib.pyplot as plt

def histogrammaker(result,key='meas',show=True):
    counts = getattr(result[0].data, key).get_counts()
    histdiag=plot_histogram(counts)
    if show:
      plt.show()
    return histdiag

def circuitvis(circuit):
    circuit_drawer(circuit, output='mpl')
    plt.show()

def generate_pdf_report(circuit,noise_model=None,result=None, key='meas',filename='sim_result.pdf'):
    """
    generate a pdf report of a sim with circuit diagram, noise model info and plots
    """
    fig1=circuit_drawer(circuit,output='mpl')
    fig, ax = plt.subplots(figsize=(8.5, 11))
    with PdfPages(filename) as pdf:
     
       plt.title("Quantum_Circuit")
       pdf.savefig(fig1)
       plt.close(fig1)
       if noise_model!=None:
         noise_text="Noise Mode Info\n\n"
         noise_text+=str(noise_model)
           # Standard A4 size
         ax.axis('off')  # Turn off axes for clean look
         ax.text(0.05, 0.95, noise_text, fontsize=12, va='top', wrap=True)
         plt.title("Noise_info")
         pdf.savefig(fig)
         plt.close(fig)
       if result!=None:
          fig2=histogrammaker(result,show=False,key=key)
          plt.title("Histogram of Counts")
          pdf.savefig(fig2)
          plt.close(fig2)
          
          
        
    print(f"report saved as {filename}")
    

