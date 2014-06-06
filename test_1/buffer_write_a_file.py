__author__ = 'fyu'

import os
import io

dir='../data/'
fname=dir+'test1.txt'

if os.path.exists(fname):
    f=io.open(fname,'w+')
else:
    f=io.open('../data/'+fname, 'w+')
for i in xrange(1,1000):
    f.writelines("%4s" % unicode(i)+': 3rd buffered hello world!\n')

f.close()
