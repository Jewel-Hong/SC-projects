"""
File: boggle.py
Name: 洪禎蔚
----------------------------------------
TODO: To find the word in the board  in any direction without repeating the same character.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

dict_lst = []
found_lst = []


def main():
	"""
	TODO: To set up the dictionary and boggle board, find the word and print the answer.
	"""
	read_dictionary()
	boggle_lst = original_settings()
	boggle(boggle_lst)
	print(f'There are {len(found_lst)} words in total.')


def boggle(boggle_lst):
	"""
	TODO: To find all the words on the board by starting with every character.
	:param boggle_lst (list): the boggle board
	"""
	for i in range(len(boggle_lst)):
		for j in range(len(boggle_lst[i])):
			cur_s = boggle_lst[i][j]
			used_position = [(i, j)]
			boggle_helper(boggle_lst, i, j, cur_s, used_position)


def boggle_helper(boggle_lst, r, c, cur_s, used_position):
	"""
	TODO: To keep the words with prefix and find the words.
	:param boggle_lst (list): the boggle board
	:param r (int): the row of the last character
	:param c (int): the column of the last character
	:param cur_s (str): current string
	:param used_position (list): the position of each character in current string 
	"""
	global found_lst
	if has_prefix(cur_s):
		# Base Case
		if len(cur_s) >= 4 and cur_s in dict_lst and cur_s not in found_lst:
			print(f'Found \"{cur_s}\"')
			found_lst.append(cur_s)
			dict_lst.remove(cur_s)
			boggle_helper(boggle_lst, r, c, cur_s, used_position)

		else:
			for i in range(-1, 2, 1):
				for j in range(-1, 2, 1):
					new_r = i + r
					new_c = j + c
					if (new_r, new_c) not in used_position:
						if 0 <= new_r < 4 and 0 <= new_c < 4:
							used_position.append((new_r, new_c))
							# choose
							cur_s += boggle_lst[new_r][new_c]
							# explore
							boggle_helper(boggle_lst, new_r, new_c, cur_s, used_position)
							# un-choose
							used_position.pop()
							cur_s = cur_s[:-1]


def original_settings():
	"""
	TODO: To set up the boggle board
	:return boggle_lst (list): the boggle board
	"""
	boggle_lst = []
	for i in range(4):
		row = input(f'{i+1} row of letters: ').lower()
		if row[1] != ' ' or row[3] != ' ' or row[5] != ' ':
			print('Illegal input')
			break
		else:
			boggle_lst.append([])
			for j in range(0, 7, 2):
				boggle_lst[i].append(row[j])
	return boggle_lst


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for word in f:
			global dict_lst
			dict_lst.append(word.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict_lst:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
