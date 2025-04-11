
from circuits.create_states import bellstategenerator
from channels.noisechannel import depolarizing_noise
from circuits.apply_noise import applynoise
from simulate.simulate import simulatecircuit
from simulate.result import interpret_result
state=bellstategenerator()
noise_model=depolarizing_noise()
alter_state,sim=applynoise(state,noise_model)
result=simulatecircuit(alter_state,sim)
interpret_result(result)
