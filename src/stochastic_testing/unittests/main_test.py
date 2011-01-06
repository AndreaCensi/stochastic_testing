import unittest

# Make sure everything is defined
from .gaussian import *
from .uniform_continuous import *
from .uniform_discrete import *

from stochastic_testing import StochasticTestManager

class StochasticTests(unittest.TestCase):
    
    def test_stochastic(self):
        StochasticTestManager.main.run(10)
