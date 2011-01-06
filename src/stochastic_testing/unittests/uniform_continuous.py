import numpy as np

from stochastic_testing import stochastic, ContinuousUniformDistribution
from stochastic_testing import stochastic_fail

@stochastic
def continuous_uniform_densities():

    def uniform_distribution_test(bounds, N):
        x = bounds[0] + np.random.rand(N) * (bounds[1] - bounds[0])
        return ContinuousUniformDistribution(x, bounds)
    
    for N in [100, 1000, 10000]:
        for bounds in [(0, 1), (0, 2), (-1, 1)]:
            yield uniform_distribution_test, bounds, N
 

@stochastic_fail
def continuous_uniform_densities_wrong():

    def wrong1(N):
        x = np.random.rand(N) * 0.9
        return ContinuousUniformDistribution(x, bounds=(0, 1))
    
    def wrong2(N):
        x = np.random.rand(N) ** 2
        return ContinuousUniformDistribution(x, bounds=(0, 1))
    
    for N in [100, 1000, 10000]:
        yield wrong1, N
        yield wrong2, N
