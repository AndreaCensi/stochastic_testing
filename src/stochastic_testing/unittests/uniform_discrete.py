import numpy as np
from scipy.stats.distributions import random_integers
from stochastic_testing import stochastic, DiscreteUniformDistribution

def sample_uniform_dist(bins, N):
    dist = np.zeros(bins, dtype='int')
    for x in random_integers(low=0, high=bins - 1, size=N):
        dist[x] += 1
    return dist

@stochastic
def dicrete_uniform_densities():

    def uniform_distribution_test(bins, N):
        x = sample_uniform_dist(bins, N)
        return DiscreteUniformDistribution(x)
    
    for N in [10, 100, 1000, 10000]:
        for bins in [1, 2, 5, 10]:
            yield uniform_distribution_test, bins, N

@stochastic
def discrete_uniform_single():
    
    def uniform_distribution_test(bins, N):
        x = sample_uniform_dist(bins, N)
        return DiscreteUniformDistribution(x)

    bins = 5
    N = 100
    return uniform_distribution_test, bins, N
