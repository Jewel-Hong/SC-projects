"""
File: basic_permutations.py
Name:
-----------------------------
This program finds all the 3-digits binary permutations
by calling a recursive function binary_permutations.
Students will find a helper function useful in advanced
recursion problems.
"""


def main():
	binary_permutations(3)


def binary_permutations(n):
	binary_permutations_helper(n, '')


def binary_permutations_helper(n, current_s):
	if len(current_s) == n:
		print(current_s)
	else:
		binary_permutations_helper(n, current_s+'0')
		binary_permutations_helper(n, current_s+'1')


if __name__ == '__main__':
	main()