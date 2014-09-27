__author__ = 'fyu'

from config import *
from prepare import updateData as ud
from prepare import prepareDataStringFile as pd
import numpy as np

exp_start_time=time.time()

bat_update_time_table=np.zeros((len(pers),max_exp_times))
tbat_update_time_table=np.zeros((len(pers),max_exp_times))
bat_update_time_medians=[]
tbat_update_time_medians=[]
bat_update_time_means=[]
tbat_update_time_means=[]
bat_update_time_maxs=[]
tbat_update_time_maxs=[]
bat_update_time_mins=[]
tbat_update_time_mins=[]
overhead_medians=[]
overhead_means=[]


# ---- open result file----
result_file=open(result_file_name,'w')
result_file.write(('Total Lines: %d\n'%num_lines))
print 'Total Lines: %d\n' % num_lines

for per in pers:
    result_file.write(('percentage = %g starts\n' % per))
    print 'percentage = %g starts\n' % per

    index=0

    # initialize times
    bat_update_time=0.0
    tbat_update_time=0.0

    for t in xrange(0,max_exp_times):
        #result_file.write('loop = %d\n' % (t+1))
        print 'loop=%d' %(t+1)
        # create data
        pd.prepareData(num_lines,bat_file_name,tbat_file_name)

        # update data list
        update_file_name=data_dir+'update'+str(per)+suffix
        pd.prepareUpdateList(per,num_lines,update_file_name)

        # update TBAT
        start1=time.time()
        ud.updateTBAT(tbat_file_name,update_file_name)
        temp1=time.time()-start1
        tbat_update_time_table[index][t]=temp1
        #tbat_update_time+=temp1

        # update BAT
        start2=time.time()
        ud.updateBAT1(bat_file_name,update_file_name)
        temp2=time.time()-start2
        bat_update_time_table[index][t]=temp2
        #bat_update_time+=temp2
        result_file.write('loop = %3d: | tbat_time | %12g | bat_time | %12g | overhead | %12g \n'
                          % (t+1, temp1,temp2,temp2/temp1))
        #print 'bat updated\n'

    tbat_update_time_medians.append(np.median(tbat_update_time_table[index]))
    tbat_update_time_means.append(np.mean(tbat_update_time_table[index]))
    tbat_update_time_maxs.append(np.max(tbat_update_time_table[index]))
    tbat_update_time_mins.append(np.min(tbat_update_time_table[index]))
    
    bat_update_time_medians.append(np.median(bat_update_time_table[index]))
    bat_update_time_means.append(np.mean(bat_update_time_table[index]))
    bat_update_time_maxs.append(np.max(bat_update_time_table[index]))
    bat_update_time_mins.append(np.min(bat_update_time_table[index]))

    overhead_medians.append(bat_update_time_medians[-1]/tbat_update_time_medians[-1])
    overhead_means.append(bat_update_time_means[-1]/tbat_update_time_means[-1])

    index+=1



result_file.write('\n')

result_file.write('tbat update time medians:\n')
for i in xrange(0, len(pers)):
    per=pers[i]
    str='%g, %g\n' % (per, tbat_update_time_medians[i])
    result_file.write(str)
result_file.write('\n')

result_file.write('tbat update time means:\n')
for i in xrange(0, len(pers)):
    per=pers[i]
    str='%g, %g\n' % (per, tbat_update_time_means[i])
    result_file.write(str)
result_file.write('\n')

result_file.write('bat update time medians:\n')
for i in xrange(0, len(pers)):
    per=pers[i]
    str='%g, %g\n' % (per, bat_update_time_medians[i])
    result_file.write(str)
result_file.write('\n')

result_file.write('bat update time means:\n')
for i in xrange(0, len(pers)):
    per=pers[i]
    str='%g, %g\n' % (per, bat_update_time_means[i])
    result_file.write(str)
result_file.write('\n')

result_file.write('median overheads:\n')
for i in xrange(0, len(pers)):
    per=pers[i]
    str='%g, %g\n' % (per, overhead_medians[i])
    result_file.write(str)
result_file.write('\n')


result_file.write('mean overheads:\n')
for i in xrange(0, len(pers)):
    per=pers[i]
    str='%g, %g\n' % (per, overhead_means[i])
    result_file.write(str)
result_file.write('\n')




# # --------write results---------
# result_file.write('\n')
# result_file.write('bat update times:\n')
# for i in xrange(0, len(pers)):
#     per=pers[i]
#     bat_update_time=bat_update_times[i]
#     str='%g, %g\n' % (per, bat_update_time)
#     result_file.write(str)
# result_file.write('\n')
#
# result_file.write('tbat update times:\n')
# for i in xrange(0, len(pers)):
#     per=pers[i]
#     tbat_update_time=tbat_update_times[i]
#     str='%g, %g\n' % (per, tbat_update_time)
#     result_file.write(str)
# result_file.write('\n')
#
# result_file.write('overheads:\n')
# for i in xrange(0, len(pers)):
#     per=pers[i]
#     overhead=overheads[i]
#     str='%g, %g\n' % (per, overhead)
#     result_file.write(str)
# result_file.write('\n')



#--------calculate total execution time------------
exp_total_time=time.time()-exp_start_time
result_file.write('Experiment completed in %gs\n' % (exp_total_time))
print 'Experiment completed in %gs\n' % (exp_total_time)
result_file.close()