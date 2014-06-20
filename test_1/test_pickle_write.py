__author__ = 'fyu'


import pickle as pk
import os

f=open('test.data','wb')

pk.dump({1:10},f)
pk.dump({2:20},f)
f.close()

