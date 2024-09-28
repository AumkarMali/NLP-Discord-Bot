# game_logic.py

import random

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["attack", "magic"]

    def gen_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
            return self.hp

    def heal(self, dmg):
        self.hp += dmg

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    async def choose_action(self, message):
        i = 1
        await message.channel.send("**Actions**")
        for item in self.actions:
            await message.channel.send(f'{str(i)}: {item}')
            i += 1

    async def choose_magic(self, message):
        await message.channel.send('1: fire (Cost: 10, damage: 110)\n2: thunder (Cost: 15, damage: 160)\n3: blizzard (Cost: 8, damage: 75)\n4: meteor (Cost: 20, damage: 205)\n5: quake (Cost: 14, damage: 132)\n6: gravity (Cost: 35, damage: 340)\n7: balance (Cost: 40, Ability: enemies HP = Players HP, effectiveness varies)\n8: trade (Cost: 0, Ability: trade 80 HP for 30 MP)\n9: cure (Cost: 12, Heal: 120)\n10: cura (Cost: 18, Heal: 200)')

class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_dmg(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)
