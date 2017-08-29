import random
from combat import Combat

class Character(Combat):
    attackLimit = 10
    experience = 0
    baseHitPoints = 10

    def attack(self):
        roll = random.randint(1, self.attackLimit)
        if self.weapon == 'sword':
            roll += 1
        elif self.weapon == 'axe':
            roll += 2
        return roll > 4

    def getWeapon(self):
        weaponChoice = input("Weapon ([S]word, [A]xe, [B]ow:) ").lower()

        if weaponChoice in 'sab':
            if weaponChoice == 's':
                return 'sword'
            if weaponChoice == 'a':
                return 'axe'
            else:
                return 'bow'
        else:
            return self.getWeapon()

    def __init__(self, **kwargs):
        self.name = input("Name: ")
        self.weapon = self.getWeapon()
        self.hitPoints = self.baseHitPoints

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{}, HP: {}, XP: {}'.format(self.name, self.hitPoints, self.experience)

    def rest(self):
        if self.hitPoints < self.baseHitPoints:
            self.hitPoints += 1

    def leveledUp(self):
        return self.experience >= 5
