## Functions for computing Relative accuracy (RA) which measures how many estimations are within a certain tolerance ##
#  given as:
#  RA = np/n * 100;    
#  where np = number of estimations within the specified tolerance
#         n = total number of values being checked
#  Percentage absolute error is given as:
#  PAE = abs(actual - predicted) / actual   

import numpy as np

def RA_10(actual, predicted):
    pae = abs(actual - predicted) / actual   
    pos = np.sum(pae<0.1)
    ra = pos/len(pae) * 100
    return ra

def RA_15(actual, predicted):
    pae = abs(actual - predicted) / actual
    pos = np.sum(pae<0.15)
    ra = pos/len(pae) * 100
    return ra

def RA_20(actual, predicted):
    pae = abs(actual - predicted) / actual
    pos = np.sum(pae<0.20)
    ra = pos/len(pae) * 100
    return ra