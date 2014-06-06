__author__ = 'fyu'

import os
dir='../data/'
fname=dir+'test1.txt'

if os.path.exists(fname):
    f=open(fname,'r+')
else:
    f=open('../data/'+fname, 'w+')
for i in xrange(1,1000):
    f.writelines(str(i)+': hello world+++!\n')

f.close()
