MONEY = 0
WITHDRAW_LIMIT = 1000


class Pypal:
    def __init__(self, username, money=MONEY, withdraw_limit=WITHDRAW_LIMIT):
        self._n = username
        self.__m = money
        self._w_l = withdraw_limit

    def withdraw(self, amount):
        if amount > self._w_l:
            print('Exceed Limit')
        else:
            if amount <= self.__m:
                self.__m -= amount
                print(f'{self._n}: {self.__m}')
            else:
                print('Error')

    # Setter, function starts with set_
    def set_name(self, new_name):
        self._n = new_name
        return self._n

    # Getter, function starts with get_
    def get_money(self):
        return self.__m


def bank():
    bank = Pypal('Jewel', money=10000, withdraw_limit=6000)
    bank.withdraw(7000)
    bank.withdraw(5000)
    bank.withdraw(6000)


if __name__ == '__main__':
    bank()

