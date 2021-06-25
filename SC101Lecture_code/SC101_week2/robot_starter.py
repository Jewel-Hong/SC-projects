from robot import Robot, Robot2, Robot3
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow()
    r3 = Robot3(166, 58, 'violet', color3='tomato', count3=5)
    b = r3.give_me_a_ball(100)
    r = r3.give_me_a_rect(50)
    window.add(b)
    window.add(r)


if __name__ == '__main__':
    main()
