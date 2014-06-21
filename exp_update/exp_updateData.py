__author__ = 'fyu'

from config import *
from prepare import updateData as ud
from prepare import prepareDataStringFile as pd

exp_start_time=time.time()

bat_update_times=[]
tbat_update_times=[]
overheads=[]

for per in pers:
    print 'percentage = %g starts' % per
    # initialize times
    bat_update_time=0.0
    tbat_update_time=0.0

    for t in xrange(0,max_exp_times):
        print 'loop = %d' % (t+1)
        # create data
        pd.prepareData(num_lines,bat_file_name,tbat_file_name)

        # update data list
        update_file_name=data_dir+'update'+str(per)+suffix
        pd.prepareUpdateList(per,num_lines,update_file_name)

        # update TBAT
        tbat_time_start=time.time()
        ud.updateTBAT(tbat_file_name,update_file_name)
        tbat_update_time+=time.time()-tbat_time_start

        # update BAT
        bat_time_start=time.time()
        ud.updateBAT(bat_file_name,update_file_name)
        bat_update_time+=time.time()-bat_time_start

    overhead=bat_update_time/tbat_update_time
    bat_update_time=bat_update_time/max_exp_times
    tbat_update_time=tbat_update_time/max_exp_times

    bat_update_times.append(bat_update_time)
    tbat_update_times.append(tbat_update_time)
    overheads.append(overhead)

#--------write results---------
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

#--------calculate total execution time------------
exp_total_time=time.time()-exp_start_time
print 'Experiment completed in %gs' % (exp_total_time)