import time
import numpy as np


class TestStatistic(object):
    def pvalue(self):
        assert False

class StochasticTest(object):
    def __init__(self, command, args):
        self.command = command
        self.args = args 
        self.results = []
        self._running_time = None
        self.command_desc = command.__name__
        
    def running_time(self):
        if self._running_time is None:
            t0 = time.clock()
            result = self.run()
            self.results.append(result)
            self._running_time = time.clock() - t0
            
        return self._running_time
        
    def run(self):
        res = self.command(*self.args)
        if not isinstance(res, TestStatistic):
            raise Exception('Test %s returned %s' % (self.command, type(res)))
        return res
    
    def run_stochastic(self, repeats):
        for i in range(repeats): #@UnusedVariable
            self.results.append(self.run())
            
        pvalues = [x.pvalue() for x in self.results]
        from stochastic_testing import ContinuousUniformDistribution
        return ContinuousUniformDistribution(pvalues)
        
    
    def __str__(self):
        return 'stoch:%s params %s' % (self.command_desc, self.args)
    
class StochasticTestManager(object):
    def __init__(self):
        self.tests = []
    
    def add_test(self, callable, *args):
        assert hasattr(callable, '__call__'), 'Expected callable, got %s' % type(callable)
        self.tests.append(StochasticTest(callable, args))

    def run(self, time_limit=10):
        print "Running %d tests; time limit is %.1f seconds" % (len(self.tests), time_limit)
        t0 = time.clock()
        
        print('Checking time')
        total = 0
        for t in self.tests:
            this = t.running_time()
            total += this
            print('- %8.5f  %s' % (this, t))
        
        remaining = time_limit - (time.clock() - t0)
        times = int(np.floor(remaining / total))
        print('I have time for %d repeats' % times) 
        
        print('Running %d repeats' % times) 
        for t in self.tests:
            pvalues = t.run_stochastic(times)
            pv = pvalues.pvalue()
            print('- pvalue %8.5f (%d samples) %s' % (pv, pvalues.samples.size, t))
            print pvalues.samples
        
        t1 = time.clock() - t0
        print("Used %f seconds" % t1)

StochasticTestManager.main = StochasticTestManager()

def stochastic(f):
    result = f()
    def add_tuple(t):
        assert isinstance(t, tuple), 'Expected tuple, got %s' % type(t)
        stm = StochasticTestManager.main
        stm.add_test(t[0], *t[1:]) 
        
    if hasattr(result, 'next'):
        for x in result:
            add_tuple(x)
    else:
        add_tuple(result)
    
    
