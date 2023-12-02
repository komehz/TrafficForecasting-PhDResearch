import numpy as np

def split(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
        
def GEH(actual, predicted):
    actual = split(actual)*4
    predicted = split(predicted)*4
    geh = np.sqrt(2 * ((predicted - actual) ** 2) / (predicted + actual))   
    count = np.sum(geh<5)
    return geh, count, actual/4, predicted/4