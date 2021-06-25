"""
File: anagram.py
Name: 洪禎蔚
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
dict_lst = []
anagrams = []


def main():
    read_dictionary()
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        else:
            print('Searching...')
            find_anagrams(s)
            print(f'{len(anagrams)} anagrams: {anagrams}')
            anagrams.clear()


def read_dictionary():
    with open(FILE, 'r') as f:
        for word in f:
            global dict_lst
            dict_lst.append(word.strip())


def find_anagrams(s):
    """
    :param s (str): the word to find the anagrams
    """
    find_anagrams_helper(s, [])


def find_anagrams_helper(s, index_lst):
    cur_s = ''
    for i in index_lst:
        cur_s += s[i]
    if has_prefix(cur_s):
        if len(cur_s) == len(s):
            if cur_s in dict_lst and cur_s not in anagrams:
                print(f'Found: {cur_s}')
                anagrams.append(cur_s)
                print('Searching...')
        else:
            for i in range(len(s)):
                if i not in index_lst:
                    index_lst.append(i)
                    find_anagrams_helper(s, index_lst)
                    index_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s (str): the sub-string to be checked whether there is a word started with it
    :return (bool): True/ False
    """
    for word in dict_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
