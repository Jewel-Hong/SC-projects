from campy.graphics.gobjects import GOval, GRect


class Robot:
    def __init__(self, height, weight, color='green'):
        self.h = height
        self.w = weight
        self.c = color

    # Instance methods
    def give_me_a_ball(self, size):
        ball = GOval(size, size)
        ball.color = self.c
        ball.filled = True
        ball.fill_color = self.c
        return ball

    def self_intro(self):
        print(f'h={self.h}/ w={self.w}')

    def bmi(self):
        height_m = self.h / 100
        print('bmi:', self.w / (height_m**2))

    # Static methods
    @staticmethod
    def say_hi():
        print('Hi!')


class Robot2(Robot):
    def __init__(self, height2, weight2, color2='green', count2=3):
        super().__init__(height2, weight2, color=color2)
        self.count2 = count2

    def count_down(self):
        for i in range(self.count2):
            print(i+1, end='...')
        print('')


class Robot3(Robot2):
    def __init__(self, height3, weight3, rect_color3, color3='green', count3=3):
        super().__init__(height3, weight3, color2=color3, count2=count3)
        self.rect = rect_color3

    def give_me_a_rect(self, size):
        rect = GRect(size, size)
        rect.color = self.rect
        rect.filled = True
        rect.fill_color = self.rect
        return rect


def main():
    print('Wooooow! This is insane!')


if __name__ == 'robot':
    print('Thx for using robot.py!!')

if __name__ == '__main__':
    print('robot.py is executing!!')
    main()  # 看看進來程式之後第一個要執行的function是哪個! Function name也可以不要叫做main
