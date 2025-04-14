
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from .plotting_result import circuitvis,histcomp,histogrammaker
from simulate.simulate import applysim,simulate_circuit
from simulate.result import measresult,operesult



def generate_pdf_report(circuit,noise_model=None,filename='results\sample_result.pdf'):
    """
    generate a pdf report of a sim with circuit diagram, noise model info and plots
    """
   
    fig1=circuitvis(circuit,show=False)
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
         
         noise_result_meas=simulate_circuit(circuit,noisemodel=noise_model)
         ideal_result_meas=simulate_circuit(circuit)
         noise_result_ope=simulate_circuit(circuit,noisemodel=noise_model,method='density_matrix')
         ideal_result_ope=simulate_circuit(circuit,method='density_matrix')
         fig2=histcomp(ideal_result_meas,noise_result_meas,show=False)
         
         plt.title("Histogram Comparison")
         pdf.savefig(fig2)
         plt.close(fig2)
         fig3, ax = plt.subplots(figsize=(9, 5))
         ax.axis("off")
         result_text=measresult(ideal_result_meas,noise_result_meas,show=False)
         result_text+=operesult(ideal_result_ope,noise_result_ope,show=False)
         ax.text(0.05, 0.95, result_text, fontsize=12, va='top', wrap=True)
         plt.title("Result_info")
         pdf.savefig(fig3)
         plt.close(fig3)

         
       else:
         ideal_result=simulate_circuit(circuit)
         fig2=histogrammaker(ideal_result,show=False)
         plt.title("Histogram of Counts")
         pdf.savefig(fig2)
         plt.close(fig2)
       
    print(f"report saved as {filename}")