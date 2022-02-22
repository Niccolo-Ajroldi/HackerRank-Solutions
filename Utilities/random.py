# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:38:26 2022

@author: nicco
"""

import random as rand

rand.seed(1)

# uniform continuous distribution [0,1]
rand.random()
a=10; b=0;
a + (rand.random() * (b - a))

# uniform doscrete distribution [a,b]
rand.randint(0,10)

# Gaussian
rand.gauss(0,1)

# random choice from list
l = [1,2,3,4,5]
rand.choice(l)

# Random Subsample From a List
rand.sample(l, 3)

# randomly shuffle a list
rand.shuffle(l)

#------------------------------------------------------------------------------
# NUMPY

import numpy.random as nprand

nprand.seed(10)

nprand.rand(10)
nprand.randint(0, 10, 20)

# Gaussian
nprand.randn(10)

