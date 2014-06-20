__author__ = 'fyu'


from prepare import prepareDataStringFile as pd
from prepare import data_dir,suffix,np

num_lines_1m=4766
num_lines=num_lines_1m*10240
pers=[0.1,0.2,0.3] # update percentage

bat_file_name=data_dir+'bat'+suffix # BAT
tbat_file_name=data_dir+'tbat'+suffix # TBAT

pd.prepareData(num_lines,bat_file_name,tbat_file_name)
print 'prepare data finished'


# update_file_names=[]
# for per in pers:
#     update_file_names.append(data_dir+'update'+str(per)+suffix) # Update File
#
# print update_file_names
