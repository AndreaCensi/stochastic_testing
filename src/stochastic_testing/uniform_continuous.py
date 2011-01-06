from scipy.stats.stats import  kstest
from .structures import TestStatistic
import numpy as np

class ContinuousUniformDistribution(TestStatistic):
    def __init__(self, samples, bounds=(0, 1), desc='Uniform distribution'):
        self.samples = np.array(samples)
        self.bounds = bounds
        self.desc = desc
        
    def pvalue(self):
        a, b = self.bounds 
        normalized = (self.samples - a) / (b - a)
        K, pvalue = kstest(normalized, 'uniform') #@UnusedVariable
        return pvalue
    
    def __str__(self):
        pval = self.pvalue()
        return '%s: %s pvalue %.5f' % (self.desc, self.dist, pval)
