"""
File: subsets.py
Name:
-------------------------
This file prints all the sub-lists on Console
by calling a recursive function - list_sub_lists(lst).
subsets.py is a famous LeetCode Medium problem
"""


def main():
    """
    LeetCode Medium Problem
    """
    list_sub_lists([1, 2, 3, 4])


def list_sub_lists(lst):
    """
    :param lst: list[str], containing a number of characters
    """
    helper(lst, [])


def helper(lst, chosen):
    if len(lst) == 0:
        print(chosen)
    else:
        # choose
        ele = lst.pop()

        # explore without
        helper(lst, chosen)

        # explore with
        chosen.append(ele)
        helper(lst, chosen)

        # un-choose
        chosen.pop()
        lst.append(ele)


if __name__ == '__main__':
    main()
