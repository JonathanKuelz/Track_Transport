import random
from copy import deepcopy

def augment_transport(in_emission):
    c_dl = deepcopy(in_emission)
    yearly_emission = 1000 * 11.61 / 365
    constant_emission = 0.75 * yearly_emission
    for idx in range(len(c_dl)):
        variable_emission = 0.5 * random.random() * constant_emission
        c_dl[idx]['co2_emission'] += variable_emission + constant_emission
    return c_dl
