__author__ = 'fyu'

import numpy as np

def reject_outliers1(data, m=2.):
    return data[abs(data - np.mean(data)) < m * np.std(data)]

def reject_outliers2(data, m = 2.):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    return data[s<m]

def reject_outliers3(data, m=0.5):
    u = np.median(data)
    s = np.std(data)
    filtered = [e for e in data if (u - m * s < e < u + m * s)]
    return filtered

a=[0.1,0.2,0.3,1,10,100,0.8]
a=[0.1, 0.15, 0.16, 0.12, 0.08, 1, 1.2]

a=reject_outliers3(a)

print a
