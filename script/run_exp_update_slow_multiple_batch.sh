#!/bin/bash
# don't forget to change your email address at the bottom

if [ -z "$1" ]
  then
    echo "Please input your email password!"
    exit
fi




num_lines_1m=47660
num_lines_1g=$(( num_lines_1m * 1024 ))
num_lines=${num_lines_1m*64}
#num_lines=100
max_exp_times=10
max_run_times=3
pers="0.1 0.2 0.3 0.4 0.5"


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
    #add category for blog
    echo "">>${tmp}

    #----email body-----
    cat data/result.txt >> ${tmp}
    #echo "hello!!!" >> ${tmp}
    #add memo file body
    echo `date` >> ${tmp}
    echo "Finished." >> ${tmp}


    sendfrom=`hostname`"your_email_address"
    sendto="to_email_address"
    smtp_server="smtp.youremail.com:587"
    xuser="your_email_user"
    xp=$1

    sendEmail -f ${sendfrom} -t ${sendto} -s ${smtp_server} -o tls=yes -xu ${xuser} -xp ${xp} -u ${title} < ${tmp}

    rm ${tmp}
    echo ${i}
done
