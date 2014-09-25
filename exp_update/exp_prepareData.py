__author__ = 'fyu'


from prepare import prepareDataStringFile as pd
#from prepare import data_dir,suffix,np
from config import *

pd.prepareData(num_lines,bat_file_name,tbat_file_name)
print 'prepare data finished'

