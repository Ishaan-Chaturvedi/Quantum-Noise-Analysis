
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from .plotting_result import circuitvis,histcomp,histogrammaker
from simulate.simulate import applysim,simulate_circuit



def generate_pdf_report(circuit,noise_model=None,filename='sim_result.pdf'):
    """
    generate a pdf report of a sim with circuit diagram, noise model info and plots
    """
    qc1=circuit.copy()
    fig1=circuitvis(qc1,show=False)
    fig, ax = plt.subplots(figsize=(8, 2))
    with PdfPages(filename) as pdf:
     
       plt.title("Quantum_Circuit")
       pdf.savefig(fig1)
       plt.close(fig1)

       if noise_model!=None:
         
         
           # Standard A4 size
         ax.axis('off')  # Turn off axes for clean look
         
         noise_text=str(noise_model)
         ax.text(0.05, 0.95, noise_text, fontsize=12, va='top', wrap=True)
         plt.title("Noise_info")
         pdf.savefig(fig)
         plt.close(fig)
         
         noise_result=simulate_circuit(circuit,noisemodel=noise_model)
         ideal_result=simulate_circuit(circuit)
         fig2=histcomp(ideal_result,noise_result,show=False)
         plt.title("Histogram Comparison")
         pdf.savefig(fig2)
         plt.close(fig2)
       else:
         ideal_result=simulate_circuit(circuit)
         fig2=histogrammaker(ideal_result,show=False)
         plt.title("Histogram of Counts")
         pdf.savefig(fig2)
         plt.close(fig2)
       
    print(f"report saved as {filename}")