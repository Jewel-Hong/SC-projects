"""
File: number_of_words.py
Name:
-------------------------------
This file calculates the number of words in
romeojuliet.txt by using word.split() and
basic Python list operations
"""

FILE = 'romeojuliet.txt'


def main():
    with open(FILE, 'r') as f:
        token_counts = 0
        for line in f:
            word_list = line.split()
            token_counts += len(word_list)
        print(f'Number of tokens: {token_counts}')


if __name__ == '__main__':
    main()

