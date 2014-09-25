__author__ = 'fyu'

import os, time, datetime
#from prepare import data_dir,suffix

max_exp_times=10




# ---------- number of lines in the testing data file---------
num_lines_1m=47660
num_lines_1g=num_lines_1m*1024

# num_lines=20
# num_lines=1000
num_lines=num_lines_1m


root_dir= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir=root_dir+'/data/'
suffix='.txt'


# ------------file location -----------------------
bat_file_name=data_dir+'bat'+suffix # BAT
tbat_file_name=data_dir+'tbat'+suffix # TBAT

#result_file_name=data_dir+'result'+time.strftime("%y%m%d-%Ih%Mm%Ss")+'.txt'
result_file_name=data_dir+'result'+'.txt'


#-------------update percentage---------------
#pers=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
pers=[0.1,0.2,0.3,0.4,0.5] # update percentage
#pers=[0.1] # update percentage






