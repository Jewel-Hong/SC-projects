"""
File: what_does_the_fox_say.py
Name: Jerry Liao
----------------------------------
This program shows the basic concepts of
Python dict by inputting data from Youtube
video What Does the Fox Say
"""


def main():
    """
    Add some sound of animals!
    """
    d = {}
    d['Dog'] = 'woof'
    d['Cat'] = 'meow'
    d['Bird'] = 'tweet'
    d['Fox'] = 'Ringdindindindineringering'
    d['Fox'] = 'Wapapapapapapow'
    print_dict(d)


def print_dict(d):
    """
    : param d: The dict containing the sound of animals
    ------------------------------------------------
    This function prints out all the key-value pairs in d
    """
    # Dict沒有index，只能用for loop!!!
    for key in d:
        value = d[key]
        print(key, '->', value)

    for key, value in d.items():
        print(key, '->', value)

if __name__ == '__main__':
    main()
