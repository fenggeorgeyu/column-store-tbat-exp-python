__author__ = 'fyu'

# BUN for BAT
class BUN:
    def __init__(self, oid, value):
        self.oid=oid
        self.value=value
    def __str__(self):
        return "(%s,%g)" % (self.oid, self.value)

# TBUN for TBAT
class TBUN(BUN):
    def __init__(self, timestamp, oid, value):
        BUN.__init__(self, oid, value)
        self.timestamp=timestamp
    def __str__(self):
        return "(%s,%s,%g)" % (self.timestamp, self.oid, self.value)


