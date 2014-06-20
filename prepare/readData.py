__author__ = 'fyu'

from config import *

bat_file=open(bat_file_name,'rb')
tbat_file=open(tbat_file_name,'rb')
update_file=open(update_file_name,'rb')

for i in xrange(0,num_lines):
    bun=pk.load(bat_file)
    print bun

try:
    while True:
        bun=pk.load(update_file)
        print bun
except (EOFError,pk.UnpicklingError, pk.UnpickleableError):
    pass


 # while (bun=pk.load(update_file))!=null:
 #     if bun!=null:
 #     print bun

bat_file.close()
tbat_file.close()
update_file.close()