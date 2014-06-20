__author__ = 'fyu'

import time, datetime
from prepare import data_dir,suffix

num_lines_1m=47660
num_lines_1g=num_lines_1m*1024
num_lines=num_lines_1m*10

bat_file_name=data_dir+'bat'+suffix # BAT
tbat_file_name=data_dir+'tbat'+suffix # TBAT

pers=range(0.1,0.1,1) # update percentage


result_file_name=data_dir+'result'+time.strftime("%y%m%d-%Ih%Mm%Ss")+'.txt'


