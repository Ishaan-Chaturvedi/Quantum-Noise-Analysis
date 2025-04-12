
from circuits.create_states import bellstategenerator,ghzstategenerator,teleportationcircuit
from channels.noisechannel import depolarizing_noise,amplitude_damping,bit_flip
from circuits.apply_noise import applynoise
from simulate.simulate import simulatenoise,simulateideal
from simulate.result import interpret_result
from result_utils.plotting_result import histogrammaker
from result_utils.plotting_result import generate_pdf_report
from result_utils.plotting_result import circuitvis


state=teleportationcircuit()
#state=ghzstategenerator()
noise_model=bit_flip()
alter_state,sim=applynoise(state,noise_model)
result=simulatenoise(alter_state,sim)
ideal_result=simulateideal(state)
interpret_result(ideal_result,key='c')
generate_pdf_report(state,noise_model,result=result,key='c')
#circuitvis(state)
