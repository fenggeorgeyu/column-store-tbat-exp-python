"""
prepare BAT, TBAT, and update list
"""

from config import *

bat_file=open(bat_file_name,'w')
tbat_file=open(tbat_file_name,'w')
update_file=open(update_file_name,'w')

np.random.seed(42)


timestamp=time.time()

# prepare BAT, TBAT

total_updated=0 # cound updated lines must <=update_lines

for i in xrange(0,num_lines):
    # prepare data
    str=bat_format  % (i+1,i+1)
    tstr=tbat_format % (timestamp,i+1,i+1)
    bat_file.write(str)
    tbat_file.write(tstr)

    # prepare update list
    rnd=np.random.uniform(0,1,1)
    if rnd <= per and total_updated < update_lines:
        # print 'rnd=%g, i=%i' %(rnd, i)
        total_updated+=1
    # only 100*per% can be updated from the original list
        update_str= bat_format  % (i+1,-1)
        update_file.write(update_str)


bat_file.close()
tbat_file.close()
update_file.close()














