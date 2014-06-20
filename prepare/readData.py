__author__ = 'fyu'

from config import *

bat_file=open(bat_file_name,'rb')
tbat_file=open(tbat_file_name,'rb')

for i in xrange(0,num_lines):
    bun=pk.load(bat_file)
    print bun

bat_file.close()
tbat_file.close()