"""
prepare files
"""
import os 

root_dir= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir=root_dir+'/data/'

bat_file_name=data_dir+'test.bat'
tbat_file_name=data_dir+'test.tbat'


# BUN for BAT
class BUN:
    def __init__(self, oid, value):
        self.oid=oid
        self.value=value
    def __str__(self):
        return "(%s,%s)" % (self.oid, self.value)


class TBUN(BUN):
    def __init__(self, timestamp, oid, value):
        BUN.__init__(self, oid, value)
        self.timestamp=timestamp
    def __str__(self):
        return "(%s,%s,%s)" % (self.timestamp, self.oid, self.value)





