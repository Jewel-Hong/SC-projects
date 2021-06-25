"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""


# The file name of our target text file
FILE = 'romeojuliet.txt'

# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'


def main():
	d = {}
	with open(FILE, 'r') as f:
		for line in f:
			token_list = line.split()
			for token in token_list:
				token = string_manipulation(token)
				# 不知道存不存在怎麼加啦! key error~
				# d[token] += 1

				# key為該文字，value為該文字出現之次數
				if token in d:
					d[token] += 1
				else:
					# 注意初始值為1，非0，因為當你看到它時是它出現的第一次!!
					d[token] = 1
		print_out_d(d)


def print_out_d(d):
	"""
	: param d: (dict) key of type str is a word
					value of type int is the word occurrence
	---------------------------------------------------------------
	This method prints out all the info in d
	"""
	for key, value in sorted(d.items(), key=lambda t: t[1]):
		print(key, '->', value)


def string_manipulation(word):
	word = word.lower()
	ans = ''
	for ch in word:
		if ch.isalpha() or ch.isdigit():
		# if ch not in PUNTUATION:
			ans += ch
	return ans


if __name__ == '__main__':
	main()
