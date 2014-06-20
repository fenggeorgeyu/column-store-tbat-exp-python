__author__ = 'fyu'


import pickle as pk
import os


f=open('test.data','rb')
v=pk.load(f)
print v[1]
v=pk.load(f)
print v[2]