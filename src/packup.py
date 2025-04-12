
from circuits.create_states import bellstategenerator
from channels.noisechannel import depolarizing_noise
from circuits.apply_noise import applynoise
from simulate.simulate import simulatenoise,simulateideal
from simulate.result import interpret_result
from result_utils.plotting_result import histogrammaker
from result_utils.plotting_result import generate_pdf_report
from result_utils.plotting_result import circuitvis


state=bellstategenerator()
noise_model=depolarizing_noise()
alter_state,sim=applynoise(state,noise_model)
result=simulatenoise(alter_state,sim)
ideal_result=simulateideal(state)
interpret_result(ideal_result)
#histogrammaker(ideal_result)
generate_pdf_report(state,result=result)
#circuitvis(state)
