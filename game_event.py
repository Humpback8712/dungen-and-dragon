from game_model import *
flag = True
import random
import time

knife = Weapon(2, '小刀')
# 初始化角色
def gamer_init():
    # 1.输入基本信息

    name = input('请输入你的名字: ')
    gender = input('请输入你的性别: ')
    # 初始装备

    package = {'weapon': ['小刀'], 'medicine': []}
    armour = {'帽子': '草帽', '上装': '短袖', '下装': '短裤', '鞋子': '草鞋'}
    blood = 100
    exp = int(0)
    ultimate_skill_list = ['none']
    location = [0, 0]
    ultimate_skill = ultimate_skill_list[0]
    while True:
        try:
            print('四项属性点共20，请分配')
            strength = int(input('设计你的力量值: '))
            dexterity = int(input('设计你的迅捷值: '))
            intelligent = int(input('设计你的智力值: '))
            fortune = int(input('设计你的运气值: '))
        except Exception as e:
            print('请输入正确数字')
        else:
            if strength + dexterity + intelligent + fortune == 20:
                break



    # 2.实例对象
    global gamer
    gamer = Person(name, gender, package, armour, blood, exp, ultimate_skill, location, strength, dexterity, intelligent, fortune)

# 引入初始化
def introduce():
    # 打开并读写初始化介绍
    print('这里是初始化介绍')

# 进行选择操作
def movement():

    # 操作列表
    print('请选择接下来你要做的操作')
    print('1.查看自身属性')
    print('2.进行移动')
    print('3.查看周围店铺')
    print('4.当前坐标位置')
    print('5.保存')
    print('6.退出')

    # 进行选择
    option = ['1', '2', '3', '4', '5', '6']
    key = input('请输入你的选择：')
    flag = False

    # 进行选择的判断，如果符合条件，则继续，若不符合，则循环，直到符合条件
    while flag == False:
        if key not in option:
            print('请输入正确选项')
            key = input('请输入你的选择：')
            flag = False
        else:
            flag = True
    return key


# 查看自身属性
def check_myself(person):

    print('*' * 100)
    print('-' * 100)
    print('玩家姓名', person.name)
    print('-' * 100)
    print('总血量', person.blood)
    print('-' * 100)
    print('经验值', person.exp)
    print('-' * 100)
    print('智力值', person.intellengent)
    print('-' * 100)
    print('敏捷值', person.dexterity)
    print('-' * 100)
    print('力量值', person.strength)
    print('-' * 100)
    print('护具', person.armour)
    print('-' * 100)
    print('背包', person.package)
    print('-' * 100)
    print('*' * 100)


# 移动函数
def move():

    gamer.walk(gamer)

# 4. 检查我的位置
def check_location():

    code = gamer.location
    print('——'*100)
    print(code)
    print('——'*100)


# 牵引函数
def traction(key):
    # 查看自身属性
    if key == '1':
        check_myself(gamer)
    elif key == '2':
        move()
    elif key == '3':
        pass
    elif key == '4':
        check_location()
    elif key == '5':
        combiat()

# 战斗函数
def combiat():

    g_blood = gamer.blood
    # 判断先攻
    monster = Monster()
    m_dex = int(monster.dex)
    g_dex = int(gamer.dexterity)
    print('你的迅捷值是：', g_dex)
    print('怪的迅捷值是：', m_dex)
    wait_check()
    if m_dex < g_dex:
        print('你的速度比怪快，于是你攻击了怪物')
        flag = dodge_monster(monster)  # 闪避判断
        if flag == 1:
            monster.been_attack(gamer)  # 玩家进攻
        next_attack = 'monster'
    else:
        # 若玩家的敏捷度小于怪，则进行运气判断。
        print('你的速度比怪慢，进行速度加成判断')
        fortune = int(gamer.fortune)
        x = random.randint(1, fortune)
        wait_check()
        print('你的运气加成是：', x)
        print('你的迅捷值加运气加成为', g_dex+x)
        if m_dex < g_dex+x:
            print('你的速度加上运气加成大于怪的速度，于是你先攻击')
            print('你攻击了怪物')
            wait_check()
            flag = dodge_monster(monster)  # 闪避判断
            if flag == 1:
                monster.been_attack(gamer)  # 玩家进攻
            next_attack = 'monster'
        else:
            print('你的速度加上运气加成还是比怪的速度慢，于是你被攻击')
            flag = dodge_gamer(gamer)  # 闪避判断
            if flag == 1:
                print('怪物攻击了你')
                next_attack = 'gamer'
                monster.attack(gamer)  # 怪物进攻
    regular_wait()
    print('这时候你的血量：', gamer.blood)
    print('这时候怪的血量：', monster.blood)
    # 死亡判断，正常循环
    while 1:
        death_check_gamer = gamer.blood
        death_check_monster = monster.blood
        print(death_check_gamer)
        if death_check_gamer <= 0:
            print('你在战斗中死亡')
            time.sleep(1)
            print('重置你的信息')
            time.sleep(1)
            print('恢复到战斗之前的状态')
            gamer.blood = g_blood
            break
        elif death_check_monster <= 0:
            print('你成功击杀怪物')
            print('获取掉落的经验值', monster.exp)
            gamer.exp = gamer.exp + monster.exp
            break
        elif next_attack == 'monster':
            time.sleep(1)
            print('怪物回合')
            monster.attack(gamer)
            next_attack = 'gamer'
            print('+' * 50)
        else:
            monster.been_attack(gamer)
            time.sleep(1)
            print('你的回合')
            next_attack = 'monster'
            print('+' * 50)

# 判定加载函数
def wait_check():

    print('正在进行判定', end='')
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('+' * 50)


# 普通加载函数
def regular_wait():

    print('正在加载中', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('+' * 50)


# 怪物闪避判断函数
def dodge_monster(monster):

    m_dex = int(monster.dex)
    print('(怪物)正在进行闪避判定，怪的迅捷值是：', m_dex)
    x = random.randint(0, m_dex)
    print('闪避结果值为：', x)
    if x < 5:
        print('闪避未成功')
        flag = 1
    else:
        print('闪避成功')
        flag = 2
    print('+' * 50)
    return flag

# 玩家闪避判断函数
def dodge_gamer(gamer):

    g_dex = int(gamer.dexterity)
    print('(你)正在进行闪避判定，你的迅捷值是：', g_dex)
    x = random.randint(0, g_dex)
    print('闪避结果值为：', x)
    if x < 5:
        print('闪避未成功（结果值）')
        flag = 1
    else:
        print('闪避成功')
        flag = 2
    print('+' * 50)

    return flag





