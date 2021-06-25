"""
File: adv_permutation.py
Name:
------------------------------
This program finds all the permutations [1, 2, 3].
To complete this task, you will need backtracking
-- choose, explore, and un-choose
"""


def main():
	permutation([1, 2, 3])


def permutation(lst):
	permutation_helper(lst, [])


def permutation_helper(lst, current_lst):
	if len(current_lst) == len(lst):
		print(current_lst)
	else:
		for num in lst:
			if num in lst:
				pass
			else:
				# Choose
				current_lst = current_lst.append(num)
				# Explore
				permutation_helper(lst, current_lst)
				# Un-choose
				current_lst.pop()  #因為lst存在heap而非stack所以要消除!


if __name__ == '__main__':
	main()