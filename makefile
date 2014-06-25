num_lines_1m=47660
num_lines_1g=48803840
num_lines_5g=244019200
num_lines_10g=488038400
# num_lines_1g=10
# num_lines_5g=10
# num_lines_10g=10

all: exp1g exp5g exp10g

exp1g:
	python -u exp_update/exp_updateData.py $(num_lines_1g) 'result1g.txt'> log_1g.txt
exp5g:
	python -u exp_update/exp_updateData.py $(num_lines_5g) 'result5g.txt'> log_5g.txt
exp10g:
	python -u exp_update/exp_updateData.py $(num_lines_10g) 'result10g.txt'> log_10g.txt
