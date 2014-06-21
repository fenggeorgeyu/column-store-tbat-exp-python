'''
updateBun bun to update
bat_file
update_file
'''
__author__ = 'fyu'
from config import *

def updateBAT(bat_file_name,update_file_name):
    bat_file=open(bat_file_name,'r+')
    update_file=open(update_file_name,'r')
    for updateLine in update_file:
        (updateLineNumStr,updateValue)=updateLine.split(',')
        updateLineNum=long(updateLineNumStr)
        # currentLineNum=1
        # while currentLineNum < updateLineNum: # simulating seeking next line
        #     # bat_file.seek(len(updateLine),1)
        #     currentLineNum+=1
        # bat_file.seek((currentLineNum-1)*len(updateLine))
        bat_file.seek((updateLineNum-1)*len(updateLine))
        bat_file.write(updateLine)
        bat_file.seek(0)
    bat_file.close()
    update_file.close()

# def updateBAT(bat_file_name,update_file_name):
#     bat_file=open(bat_file_name,'r+')
#     update_file=open(update_file_name,'r')
#     for updateLine in update_file:
#         updateLineNum=long(updateLine.split(',')[0])
#         seekLine=0
#         bat_file.seek(0)
#         for currentLine in bat_file: # simulate seeking the line to change
#             currentLineNum=long(currentLine.split(',')[0])
#             if currentLineNum == updateLineNum:
#                 #print 'change line: %d' % (currentLineNum)
#                 bat_file.seek(seekLine*len(currentLine))
#                 bat_file.write(updateLine)
#                 break
#             else:
#                 seekLine+=1
#     bat_file.close()
#     update_file.close()


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

'''
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
'''

if __name__=='__main__':
    bat_time_start=time.time()
    updateBAT(bat_file_name,update_file_name)
    bat_time=time.time()-bat_time_start
    print 'bat update time:'+str(bat_time)

    tbat_time_start=time.time()
    updateTBAT(tbat_file_name,update_file_name)
    tbat_time=time.time()-tbat_time_start
    print 'tbat update time:'+str(tbat_time)

    overhead=(bat_time)/tbat_time*100
    print 'overhead=%g%%' % (overhead)


'''
def updateBAT(bat_file_name,update_file_name):
    bat_file=open(bat_file_name,'r+')
    update_file=open(update_file_name,'r')
    for updateLine in update_file:
        (updateLineNumStr,updateValue)=updateLine.split(',')
        #print updateLineNumStr+','+updateValue
        updateLineNum=long(updateLineNumStr)
        bat_file.seek((updateLineNum-1)*len(updateLine))
        bat_file.write(updateLine)
    bat_file.close()
    update_file.close()
'''