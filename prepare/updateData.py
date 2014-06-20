__author__ = 'fyu'

from config import *

"""
updateBun bun to update
bat_file
update_file
"""

def updateBAT(bat_file_name,update_file_name):
    bat_file=open(bat_file_name,'r+')
    update_file=open(update_file_name,'r')
    for updateLine in update_file:
        (updateLineNumStr,updateValue)=updateLine.split(',')
        #print updateLineNumStr+','+updateValue
        updateLineNum=int(updateLineNumStr)
        bat_file.seek((updateLineNum-1)*len(updateLine))
        bat_file.write(updateLine)
    bat_file.close()
    update_file.close()

def updateTBAT(tbat_file_name,update_file_name):
    updateTimeStamp=time.time()
    tbat_file=open(tbat_file_name,'a')
    update_file=open(update_file_name,'r')
    for updateLine in update_file:
        updateLine='%10g,%s' %(updateTimeStamp,updateLine)
        # print updateLine
        tbat_file.write(updateLine)
    tbat_file.close()
    update_file.close()

bat_time_start=time.time()
updateBAT(bat_file_name,update_file_name)
bat_time=time.time()-bat_time_start
print 'bat update time:'+str(bat_time)

tbat_time_start=time.time()
updateTBAT(tbat_file_name,update_file_name)
tbat_time=time.time()-tbat_time_start
print 'tbat update time:'+str(tbat_time)

overhead=(bat_time-tbat_time)/bat_time*100
print 'overhead=%g%%' % (overhead)