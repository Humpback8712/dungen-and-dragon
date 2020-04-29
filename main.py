from game_model import *
import time
from game_event import *


if __name__ == '__main__':

    introduce()
    gamer_init()
    print('欢迎，开始你的征程！')
    print('*'*50)

    # 开始游戏主循环
    while True:
        print('这里是指导语句')

        # 选择操作
        key = movement()
        regular_wait()
        if key == '5':
            print('再见')
            break
        traction(key)
        print('按空格键和回车继续')

        while 1:
            x = input()
            if x == ' ':
                print('加载中...')
                break










