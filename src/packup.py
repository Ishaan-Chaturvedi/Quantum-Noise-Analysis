
from circuits.create_states import bellstategenerator,ghzstategenerator,teleportationcircuit
from channels.noisechannel import depolarizing_noise,amplitude_damping,bit_flip
from simulate.simulate import simulate_circuit
from result_utils.plotting_result import histogrammaker,circuit_drawer,histcomp
from result_utils.pdfmaker import generate_pdf_report



circuit=bellstategenerator()
noise_model=depolarizing_noise(p1=0.3,p2=0.2)
generate_pdf_report(circuit,noise_model)



