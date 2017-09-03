# -*- coding: utf-8 -*-
"""module distributions gaussiennes"""

import numpy as np

from scipy.stats import norm, multivariate_normal

def uninorm( x, mu, var ) :
    return norm.pdf( x, loc=mu, scale=var )

def multinorm( x, mu, covar ) :
    d, n = size(x)
    return multivariate_normal.pdf( x, mean=mu, cov=covar )
