import random


def augment_transport(emission_dl):
    yearly_emission = 1000 * 11.61 / 365
    constant_emission = 0.75 * yearly_emission
    for idx in range(len(emission_dl)):
        variable_emission = 0.5 * random.random() * constant_emission
        emission_dl[idx]['co2_emission'] += variable_emission + constant_emission
    return emission_dl
