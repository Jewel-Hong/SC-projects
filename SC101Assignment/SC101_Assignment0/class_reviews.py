"""
File: class_reviews.py
Name: 洪禎蔚
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    TODO: Get the maximum, minimum and average score of class SC001 and SC101 respectively.
    """
    cl = input('Which class? ').upper()
    if cl == '-1':
        print('No class scores were entered')
    else:
        score = int(input('Score: '))
        n0 = 0
        n1 = 0
        max001 = float('NaN')
        min001 = float('NaN')
        avg001 = float('NaN')
        max101 = float('NaN')
        min101 = float('NaN')
        avg101 = float('NaN')
        if cl == 'SC001':
            n0 += 1
            max001 = score
            min001 = score
            avg001 = float(score)
        elif cl == 'SC101':
            n1 += 1
            max101 = score
            min101 = score
            avg101 = float(score)
        while True:
            cl = input('Which class? ').upper()
            if cl == '-1':
                break
            else:
                score = int(input('Score: '))
                if cl == 'SC001':
                    if n0 == 0:
                        n0 += 1
                        max001 = score
                        min001 = score
                        avg001 = float(score)
                    else:
                        n0 += 1
                        max001 = maximum(score, max001)
                        min001 = minimum(score, min001)
                        avg001 = avg(score, avg001, n0)
                elif cl == 'SC101':
                    if n1 == 0:
                        n1 += 1
                        max101 = score
                        min101 = score
                        avg101 = float(score)
                    else:
                        n1 += 1
                        max101 = maximum(score, max101)
                        min101 = minimum(score, min101)
                        avg101 = avg(score, avg101, n1)
        result(max001, min001, avg001, max101, min101, avg101, n0, n1)


def result(max001, min001, avg001, max101, min101, avg101, n0, n1):
    """
    :param max001: int, the maximum among scores of SC001
    :param min001: int, the minimum among scores of SC001
    :param avg001: float, the average among scores of SC001
    :param max101: int, the maximum among scores of SC101
    :param min101: int, the minimum among scores of SC101
    :param avg101: float, the average among scores of SC101
    :param n0: int, the number of the scores of SC001
    :param n1: int, the number of the scores of SC101
    TODO: print the result
    """
    equal()
    print('SC001', end='')
    equal()
    if n0 == 0:
        print('\nNo score for SC001')
    else:
        print('\nMax (001): ' + str(max001))
        print('Min (001): ' + str(min001))
        print('Avg (001): ' + str(avg001))
    equal()
    print('SC101', end='')
    equal()
    if n1 == 0:
        print('\nNo score for SC101')
    else:
        print('\nMax (101): ' + str(max101))
        print('Min (101): ' + str(min101))
        print('Avg (101): ' + str(avg101))


def equal():
    """
    TODO: print 13 equals continuously
    """
    for i in range(13):
        print('=', end='')


def maximum(a, b):
    """
    :param a: int, any number
    :param b: int, any number
    :return: the bigger one
    """
    if a >= b:
        return a
    else:
        return b


def minimum(a, b):
    """
    :param a: int, any number
    :param b: int, any number
    :return: the smaller one
    """
    if a <= b:
        return a
    else:
        return b


def avg(new, avg, times):
    """
    :param new: int, the new score
    :param avg: float, the average of score of the class
    :param times: int, numbers of the scores of the class
    :return: float, the new average
    """
    new_avg = (avg * (times - 1) + new) / times
    return new_avg


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
