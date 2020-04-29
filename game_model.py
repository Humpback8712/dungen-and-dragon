

class Person:

    def __init__(self, name, package, armour, blood, exp, ultimate_skill, location, strength, dexterity, intellengent, fortune):
        self.name = name
        self.package = package
        self.armour = armour
        self.blood = blood
        self.exp = int(exp)
        self.ultimate_skill = ultimate_skill
        self.location = location
        self.strength = strength
        self.dexterity = dexterity
        self.intellengent = intellengent
        self.fortune = fortune

    def walk(self, person):

        code = self.location
        now_x = code[0]
        now_y = code[1]
        flag = False
        while 1:
            try:
                direction = input('请输入你的方向(北n南s西w东e):')
                length = int(input('请输入你的距离:'))
            except Exception as e:
                print('请输入正确的命令')
            else:
                location = person.location
                print('你之前的位置', location)
                break

        try:
            if direction == 'n':
                next_locatation = now_y + length
                new_locate = [now_x, next_locatation]
            elif direction == 's':
                next_location = now_y - length
                new_locate = [now_x, next_location]
            elif direction == 'w':
                next_location = now_x - length
                new_locate = [next_location, now_y]
            elif direction == 'e':
                next_location = now_x + length
                new_locate = [next_location, now_y]
            self.location = new_locate
        except Exception as e:
            print('没有这个方向，你只能选择 上北（n）下南（s）左西（w）右东（e）')
        else:
            location = person.location
            print('你现在的位置', location)


    def dodge(self):

        print('你躲避了它的技能！！！')


class Shop:
    pass


class Monster:

    def __init__(self, strength=10, blood=20, dex=5):
        self.strength = int(strength)  # 力量
        self.blood = int(blood)  # 血量
        self.dex = int(dex)  # 敏捷
        exp = self.strength + self.blood + self.dex
        self.exp = exp

    def attack(self, gamer):

        x = self.strength
        gamer.blood = gamer.blood - x

    def dodge(self):

        print('它躲避了你的技能！！！')

    def been_attack(self, gamer):

        package = gamer.package
        weapon = package['weapon']
        print('你用（' + weapon + '）攻击了怪物')
        self.blood = int(self.blood) - int(gamer.strength)


class Weapon:

    def __init__(self, aggressivity, name):
        self.aggressivity = aggressivity
        self.name = name

    def __str__(self):
        return self.name

















