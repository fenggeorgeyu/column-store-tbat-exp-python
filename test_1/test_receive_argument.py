__author__ = 'fyu'

import sys

sysarray=sys.argv
num_lines=int(sys.argv[1])
max_exp_times=int(sys.argv[2])
pers=[]

for per in sys.argv[3:-1]:
    pers.append(float(per))

print 'num_lines: %d\n' % num_lines
print 'max exp times: %d\n' % max_exp_times
print 'pers: %s' % pers


