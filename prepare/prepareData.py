"""
prepare BAT, TBAT, and update list
"""

from config import *

bat_file=open(bat_file_name,'wb')
tbat_file=open(tbat_file_name,'wb')
update_file=open(update_file_name,'wb')

np.random.seed(42)

# for i in xrange(1,10):
#     rnd=np.random.uniform(0,100,1)
#     print rnd

timestamp=time.time()

# prepare BAT, TBAT

for i in xrange(0,num_lines):
    # prepare data
    bun=BUN(i+1,i+1)
    tbun=TBUN(timestamp,i+1,i+1)
    pk.dump(bun,bat_file)
    pk.dump(tbun,tbat_file)

    # prepare update list
    rnd=np.random.uniform(0,1,1)
    if rnd <= per: #only 100*per% can be updated from the original list
        update_bun=BUN(i+1,np.random.uniform(1,100,1))
        pk.dump(update_bun, update_file)





bat_file.close()
tbat_file.close()
update_file.close()














