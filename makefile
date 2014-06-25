num_lines_1m=47660
num_lines_1g=48803840
num_lines_5g=244019200
num_lines_10g=488038400

all: exp1g exp5g exp10g
exp1g:
	nohup python -u exp_update/exp_updateData.py $(num_lines_1g) 'result1g.txt'> log_1g.txt 2>error1g.txt&
exp5g:
	nohup python -u exp_update/exp_updateData.py $(num_lines_5g) 'result5g.txt'> log_5g.txt 2>error5g.txt&
exp10g:
	nohup python -u exp_update/exp_updateData.py $(num_lines_10g) 'result10g.txt'> log_10g.txt 2>error10g.txt&
