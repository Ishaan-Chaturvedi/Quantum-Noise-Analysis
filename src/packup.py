
from circuits.create_states import bellstategenerator,ghzstategenerator,teleportationcircuit
from channels.noisechannel import depolarizing_noise,amplitude_damping,bit_flip
from circuits.apply_noise import applynoise
from simulate.simulate import simulatenoise,simulateideal
from simulate.result import interpret_result
from result_utils.plotting_result import histogrammaker,circuit_drawer,histcomp
from result_utils.pdfmaker import generate_pdf_report



circuit=teleportationcircuit()
#state=ghzstategenerator()
noise_model=bit_flip()
alter_state,sim=applynoise(circuit,noise_model)
noise_result=simulatenoise(alter_state,sim)
ideal_result=simulateideal(circuit)
#interpret_result(ideal_result)
#histcomp(ideal_result,noise_result)
generate_pdf_report(circuit)
#circuitvis(state)
