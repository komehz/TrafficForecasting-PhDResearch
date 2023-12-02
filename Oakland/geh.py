import numpy as np

def GEH(actual, predicted):
    actual = actual * 12
    predicted = predicted * 12
    geh = np.sqrt(2 * ((predicted - actual) ** 2) / (predicted + actual))   
    count = np.sum(geh<5)
    return geh, count