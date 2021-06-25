from pypal import Pypal


def main():
    bank = Pypal('Jewel', money=10000, withdraw_limit=6000)
    bank.withdraw(7000)
    bank.withdraw(5000)
    bank.withdraw(6000)
    name = bank.set_name('Guagua')
    bank.withdraw(3000)
    money = bank.get_money()
    print(name, money)


if __name__ == '__main__':
    main()
