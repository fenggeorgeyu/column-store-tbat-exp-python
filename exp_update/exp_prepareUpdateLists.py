__author__ = 'fyu'


from config import *
from prepare import prepareDataStringFile as pd


update_file_names=[]
for per in pers:
    # Update File Name e.g. update0.1.txt
    update_file_name=data_dir+'update'+str(per)+suffix
    pd.prepareUpdateList(per,num_lines,update_file_name)

print 'Update lists created.'