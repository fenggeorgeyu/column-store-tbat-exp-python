__author__ = 'fyu'

from config import *
from prepare import updateData as ud
from prepare import prepareDataStringFile as pd

bat_update_times=[]
tbat_update_times=[]
overheads=[]

for per in pers:
    pd.prepareData(num_lines,bat_file_name,tbat_file_name)
    print 'prepare data finished'

        # Update File Name e.g. update0.1.txt
    update_file_name=data_dir+'update'+str(per)+suffix
    pd.prepareUpdateList(per,num_lines,update_file_name)

    print 'Update lists created for percentage=%g' %per

    update_file_name=data_dir+'update'+str(per)+suffix

    #print 'update: '+bat_file_name
    bat_time_start=time.time()
    ud.updateBAT(bat_file_name,update_file_name)
    bat_update_time=time.time()-bat_time_start
    #print 'bat update time:'+str(bat_time)
    bat_update_times.append(bat_update_time)

    # print 'update: '+tbat_file_name
    tbat_time_start=time.time()
    ud.updateTBAT(tbat_file_name,update_file_name)
    tbat_update_time=time.time()-tbat_time_start
    #print 'tbat update time:'+str(tbat_time)
    tbat_update_times.append(tbat_update_time)

    overhead=bat_update_time/tbat_update_time*100.00
    #print 'overhead=%g%%' % (overhead)
    overheads.append(overhead)

result_file=open(result_file_name,'w')
result_file.write('bat update times:\n')
for i in xrange(0, len(pers)):
    per=pers[i]
    bat_update_time=bat_update_times[i]
    str='%g: %g\n' % (per, bat_update_time)
    result_file.write(str)
result_file.write('\n')

result_file.write('tbat update times:\n')
for i in xrange(0, len(pers)):
    per=pers[i]
    tbat_update_time=tbat_update_times[i]
    str='%g: %g\n' % (per, tbat_update_time)
    result_file.write(str)
result_file.write('\n')

result_file.write('overheads:\n')
for i in xrange(0, len(pers)):
    per=pers[i]
    overhead=overheads[i]
    str='%g: %g\n' % (per, overhead)
    result_file.write(str)
result_file.write('\n')

result_file.close()