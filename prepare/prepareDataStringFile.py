"""
prepare BAT, TBAT, and update list
"""

from config import *

def prepareData(num_lines, bat_file_name, tbat_file_name):

    bat_file=open(bat_file_name,'w')
    tbat_file=open(tbat_file_name,'w')
    bat_file.truncate()
    tbat_file.truncate()

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
    update_file.truncate()
    # --------- prepare update list -----------
    update_num_lines=long(per*num_lines)
    total_updated=0
    currentLine=1
    np.random.seed(42)
    while total_updated < update_num_lines: # draw total of update_num_lines
        rnd=np.random.uniform(0,1)
        if rnd <= 0.1: #!fixed prob to draw
            total_updated+=1
            update_str= bat_format  % (currentLine,-1)
            update_file.write(update_str)
            #print 'update line: %d' % (currentLine)
        if currentLine < num_lines:
            currentLine+=1 # move to next line
        else:
            currentLine=1
            # !!! loop back to 1, otherwise over num_lines will
            #  not be updated !!!

    #print 'total updated: %d' % (total_updated)
    update_file.close()







