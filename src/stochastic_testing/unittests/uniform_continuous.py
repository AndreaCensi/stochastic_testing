import numpy as np

from stochastic_testing import stochastic, ContinuousUniformDistribution

@stochastic
def continuous_uniform_densities():

    def uniform_distribution_test(bounds, N):
        x = bounds[0] + np.random.rand(N) * (bounds[1] - bounds[0])
        return ContinuousUniformDistribution(x)
    
    for N in [10, 100, 1000, 10000]:
        for bounds in [(0, 1), (0, 2), (-1, 1)]:
            yield uniform_distribution_test, bounds, N
 
