"""
File: dice_rolls_sum.py
Name:
-----------------------------
This program finds all the dice rolls permutations
that sum up to a constant TOTAL. Students will find
early stopping a good strategy of decreasing the number
of recursive calls
"""

# This constant controls the sum of dice of our interest
TOTAL = 8


def main():
    count = []
    dice_sum(TOTAL, [], count)
    print(sum(count))


def dice_sum(target_sum, current_lst, count):
    count.append(1)

    if sum(current_lst) == target_sum:
        print(current_lst)
    else:
        for num in [1, 2, 3, 4, 5, 6]:
            current_lst.append(num)
            if sum(current_lst) <= target_sum:
                dice_sum(target_sum, current_lst, count)
            current_lst.pop()


if __name__ == '__main__':
    main()
