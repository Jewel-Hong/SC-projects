"""
File: coin_flip_runs.py
Name: 洪禎蔚
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r


def main():
	"""
	TODO: Print the result of coin-flipping that fits the number of runs.
	"""
	print('Let\'s flip a coin!')
	num_run = int(input('Number of runs: '))
	ht = ('H', 'T')
	result = r.choice(ht)
	while True:
		result += r.choice(ht)
		if finish(result, num_run):
			break
	print(result[0: len(result)-1])


def finish(result, num_run):
	"""
	:param result: str, the string that composed randomly by H and T
	:param num_run: int, the number of runs that the player decided
	:return: bool, return when the result fits the number of runs
	"""
	n = 0
	for i in range(len(result)-2):
		if result[i] == result[i+1] and result[i+1] != result[i+2]:
			n += 1
			if n == num_run:
				return True


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
