__author__ = 'fyu'

from prepare import prepareDataStringFile as pd
from prepare import data_dir,suffix,np


num_lines=1000

bat_file_name=data_dir+'bat'+suffix # BAT
tbat_file_name=data_dir+'tbat'+suffix # TBAT

pers=[0.1,0.2,0.3] # update percentage

update_file_names=[]
for per in pers:
    update_file_names.append(data_dir+'update'+str(per)+suffix) # Update File