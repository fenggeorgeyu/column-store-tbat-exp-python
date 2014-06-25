__author__ = 'fyu'

from config import *
from prepare import updateData as ud
from prepare import prepareDataStringFile as pd

exp_start_time=time.time()

bat_update_times=[]
tbat_update_times=[]
overheads=[]


# # ---- open result file----
# result_file=open(result_file_name,'w')
# result_file.write(('Total Lines: %d\n'%num_lines))

print ('Total Lines: %d\n'%num_lines)

for per in pers:
    str1=('\npercentage = %g starts' % per)
    # result_file.write(str1+'\n')
    print(str1)

    # initialize times
    bat_update_time=0.0
    tbat_update_time=0.0

    for t in xrange(0,max_exp_times):
        str1='loop = %d' % (t+1)
        # result_file.write(str1+'\n')
        print(str1)
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
        ud.updateBATFast(bat_file_name,update_file_name)
        bat_update_time+=time.time()-bat_time_start

    overhead=bat_update_time/tbat_update_time
    bat_update_time=bat_update_time/max_exp_times
    tbat_update_time=tbat_update_time/max_exp_times

    bat_update_times.append(bat_update_time)
    tbat_update_times.append(tbat_update_time)
    overheads.append(overhead)



print('\n')
print('bat update times:')
for i in xrange(0, len(pers)):
    per=pers[i]
    bat_update_time=bat_update_times[i]
    str1='%g, %g' % (per, bat_update_time)
    print(str1)

print('')


print('tbat update times:')
for i in xrange(0, len(pers)):
    per=pers[i]
    tbat_update_time=tbat_update_times[i]
    str1='%g, %g' % (per, tbat_update_time)
    print(str1)
print('')


print('overheads:')
for i in xrange(0, len(pers)):
    per=pers[i]
    overhead=overheads[i]
    str1='%g, %g' % (per, overhead)
    print(str1)
print('')



#--------calculate total execution time------------
exp_total_time=time.time()-exp_start_time
str1='Experiment completed in %ds'%exp_total_time
print(str1)
