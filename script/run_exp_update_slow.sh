#!/bin/bash

if [ -z "$1" ]
  then
    echo "Please input your email password!"
    exit
fi

now=$(date +%Y%m%d-%Hh%Mm%Ss)

num_lines_1m=47660
num_lines_1g=$(( num_lines_1m * 1024 ))
#num_lines=${num_lines_1m}
num_lines=100
max_exp_times=10
pers="0.1 0.2 0.3 0.4 0.5"

cd ..

python exp_update/exp_updateData3.py ${num_lines} ${max_exp_times} ${pers}

#---send email when finished
echo -e "sending email to me"
tmp=temp_email
title="TBAT Exp "${now}
touch ${tmp}
#add category for blog
echo "">>${tmp}

#----email body-----
cat data/result.txt >> ${tmp}
#echo "hello!!!" >> ${tmp}
#add memo file body
echo `date` >> ${tmp}
echo "Finished." >> ${tmp}


sendfrom=`hostname`"<fengyu@siu.edu>"
sendto="fengyu@siu.edu"
smtp_server="smtp.gmail.com:587"
xuser="fengyu@siu.edu"
xp=$1

sendEmail -f ${sendfrom} -t ${sendto} -s ${smtp_server} -o tls=yes -xu ${xuser} -xp ${xp} -u ${title} < ${tmp}

rm ${tmp}

