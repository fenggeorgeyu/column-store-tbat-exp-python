#!/bin/bash

if [ -z "$1" ]
  then
    echo "Please input your email password!"
    exit
fi

# change to your own email settings

##sendfrom=`hostname`"your_email_address"
##sendto="to_email_address"
##smtp_server="smtp.youremail.com:587"
##xuser="your_email_user"

#sendfrom=`hostname`"fyu@ysu.edu"
sendfrom="fyu@ysu.edu"
sendto="fyu@ysu.edu"
smtp_server="smtp.office365.com:587"
xuser="fyu@ysu.edu"
xp=$1 #email password

# experiment parameter settings
num_lines_1m=47660 # 1MB BAT lines
num_lines_1g=$(( num_lines_1m * 1024 )) # 1GB
size_num=1
num_lines=$(( num_lines_1m  * size_num )) # current using size
#num_lines=1000
max_run_times=1 # total run times in the entire experiment
max_exp_times=3 # total loop times in each run

#pers="0.1 0.2 0.3 0.4 0.5"
pers="0.1 0.15 0.2 0.25 0.3"


cd ..

for (( i=1; i<=max_run_times; i++ ))
do
    now=$(date +%Y%m%d-%Hh%Mm%Ss)
    python exp_update/exp_updateData3.py ${num_lines} ${max_exp_times} ${pers}
    cp data/result.txt data/result-l${num_lines}-expt-${max_exp_times}${now}.txt

    #---send email when finished
    echo -e "sending email to me"
    tmp=temp_email
    title="TBAT Exp on "`hostname`" at "${now}
    touch ${tmp}
    echo "">>${tmp}

    #----email body-----
    cat data/result.txt >> ${tmp}
    echo `date` >> ${tmp}
    echo "Finished." >> ${tmp}



    sendEmail -f ${sendfrom} -t ${sendto} -s ${smtp_server} -o tls=yes -xu ${xuser} -xp ${xp} -u ${title} < ${tmp}

    rm ${tmp}
    echo ${i}
done
