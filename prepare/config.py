__author__ = 'fyu'

import os,sys,time,datetime
import cPickle as pk
import numpy as np
from base_class import BUN,TBUN

root_dir= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir=root_dir+'/data/'

suffix='.txt'
bat_file_name=data_dir+'bat'+suffix # BAT
tbat_file_name=data_dir+'tbat'+suffix # TBAT
update_file_name=data_dir+'update'+suffix # Update File

bat_format='%10d,%10d\n'
tbat_format='%10g,%10d,%10d\n'

num_lines=100000 # total lines for BAT and TBAT

per=0.20 # percentage of update of the original table size
update_lines=int(np.floor(per*num_lines))

# print update_lines