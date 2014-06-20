"""
prepare BAT, TBAT, and update list
"""

from config import *

def prepareData(num_lines, bat_file_name, tbat_file_name):
    bat_file=open(bat_file_name,'w')
    tbat_file=open(tbat_file_name,'w')
    timestamp=time.time()
    # --------- prepare BAT, TBAT -----------
    for i in xrange(0,num_lines):
        # prepare data
        str=bat_format  % (i+1,0)
        tstr=tbat_format % (timestamp,i+1,0)
        bat_file.write(str)
        tbat_file.write(tstr)
    bat_file.close()
    tbat_file.close()


def prepareUpdateList(per, num_lines, update_file_name):
    update_file=open(update_file_name,'w')
    # --------- prepare update list -----------
    #print 'total lines: %d' % num_lines
    update_num_lines=long(per*num_lines)
    #print 'total update lines: %d' % update_num_lines
    total_updated=0 # cound updated lines must <=update_lines
    for i in xrange(0,num_lines):
        # prepare update list
        rnd=np.random.uniform(0,1,1)
        if rnd <= per and total_updated < update_num_lines:
            total_updated+=1
        # only 100*per% can be updated from the original list
            update_str= bat_format  % (i+1,-1)
            update_file.write(update_str)
    update_file.close()







