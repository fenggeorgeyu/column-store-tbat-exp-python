num_lines_1m=47660
num_lines_1g=48803840
num_lines_5g=244019200
num_lines_10g=488038400
# num_lines_1g=10000
# num_lines_5g=10000
# num_lines_10g=10000

all: start_time exp1g exp5g exp10g end_time

start_time:
	echo 'Experiment started at:'`date '+%c'`
	date '+%s' > time_tmp;
end_time:
	read st < time_tmp; echo 'Experiment finished in: '$$((`date '+%s'`-$$st))'sec'; rm time_tmp; \
	echo 'Experiment finished at:'`date '+%c'`
exp1g:
	python -u exp_update/exp_updateData.py $(num_lines_1g) > log_1g.txt
exp5g:
	python -u exp_update/exp_updateData.py $(num_lines_5g) > log_5g.txt
exp10g:
	python -u exp_update/exp_updateData.py $(num_lines_10g) > log_10g.txt
