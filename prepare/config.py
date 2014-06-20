__author__ = 'fyu'

import os,sys,time,datetime
import pickle as pk
import numpy as np
from base_class import BUN,TBUN

root_dir= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir=root_dir+'/data/'

bat_file_name=data_dir+'bat.data' # BAT
tbat_file_name=data_dir+'tbat.data' # TBAT
update_file_name=data_dir+'update.data' # Update File

num_lines=20 # total lines for BAT and TBAT

per=0.2 # percentage of update of the original table size