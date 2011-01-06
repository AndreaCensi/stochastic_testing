from scipy.stats.stats import  kstest
from .structures import TestStatistic
import numpy as np

class ContinuousUniformDistribution(TestStatistic):
    def __init__(self, samples, a=0, b=1, desc='Uniform distribution'):
        self.samples = np.array(samples)
        self.a = a
        self.b = b
        self.desc = desc
        
    def pvalue(self):
        normalized = (self.samples - self. a) / (self.b - self.a)
        K, pvalue = kstest(normalized, 'uniform') #@UnusedVariable
        return pvalue
    
    def __str__(self):
        pval = self.pvalue()
        return '%s: %s pvalue %.5f' % (self.desc, self.dist, pval)
