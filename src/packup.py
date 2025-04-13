
from circuits.create_states import bellstategenerator,ghzstategenerator,teleportationcircuit
from channels.noisechannel import depolarizing_noise,amplitude_damping,bit_flip
from simulate.simulate import simulate_circuit
from simulate.result import interpret_result, measurement_fidelity, operator_fidelity
from result_utils.plotting_result import histogrammaker,circuit_drawer,histcomp
from result_utils.pdfmaker import generate_pdf_report



circuit=bellstategenerator()
#state=ghzstategenerator()
noise_model=depolarizing_noise(p1=0.3,p2=0.2)
noise_result=simulate_circuit(circuit,noisemodel=noise_model,method='density_matrix')
ideal_result=simulate_circuit(circuit,method='density_matrix')
#interpret_result(noise_result,prob=True,show=True)
fid=operator_fidelity(ideal_result,noise_result)
print(fid)

#interpret_result(ideal_result)
#histcomp(ideal_result,noise_result)
generate_pdf_report(circuit,noise_model)
#circuitvis(stat


