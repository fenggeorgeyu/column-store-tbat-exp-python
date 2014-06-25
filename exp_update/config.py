__author__ = 'fyu'

import time, datetime, sys
from prepare import data_dir,suffix

max_exp_times=10

if len(sys.argv)<=1:
    num_lines_1m=47660 #1MB data
    num_lines_1g=num_lines_1m*1024 #1GB data
    num_lines=num_lines_1m
    # num_lines=20
    # num_lines=1000
else:
    num_lines=long(sys.argv[1])

bat_file_name=data_dir+'bat'+suffix # BAT
tbat_file_name=data_dir+'tbat'+suffix # TBAT

#pers=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] # update percentage
pers=[0.1,0.2,0.3,0.4,0.5] # update percentage
#pers=[0.1] # update percentage



