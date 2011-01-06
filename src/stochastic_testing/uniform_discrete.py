from scipy.stats.stats import chisqprob, kstest
from .structures import TestStatistic

def uniform_dist_pvalue(dist):
    # http://en.wikipedia.org/wiki/Pearson's_chi-square_test#Discrete_uniform_distribution
    Ei = dist.sum() / dist.size
    Oi = dist
    chi2 = ((Ei - Oi) ** 2 / Ei).sum()
    pvalue = chisqprob(chi2, dist.size - 1) 
    return pvalue 
        
class DiscreteUniformDistribution(TestStatistic):
    def __init__(self, dist, desc='Uniform distribution'):
        assert dist.dtype == 'int', str(dist.dtype)
        self.dist = dist
        self.desc = desc

    def pvalue(self):
        return uniform_dist_pvalue(self.dist)
    
    def __str__(self):
        pval = self.pvalue()
        return '%s: %s pvalue %.5f' % (self.desc, self.dist, pval)
