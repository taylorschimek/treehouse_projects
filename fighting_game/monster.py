import random

from combat import Combat

COLORS = ['yellow', 'red', 'blue', 'green']


class Monster(Combat):
    minHitPoints = 1
    maxHitPoints = 1
    minExperience = 1
    maxExperience = 1
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.hitPoints = random.randint(self.minHitPoints, self.maxHitPoints)
        self.experience = random.randint(self.minExperience, self.maxExperience)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hitPoints,
                                              self.experience)

    def battlecry(self):
        return self.sound.upper()


class Goblin(Monster):
    maxHitPoints = 3
    maxExperience = 2
    sound = 'squeak'

class Troll(Monster):
    minHitPoints = 3
    maxHitPoints = 5
    minExperience = 2
    maxExperience = 6
    sound = 'growl'

class Dragon(Monster):
    minHitPoints = 5
    maxHitPoints = 18
    minExperience = 6
    maxExperience = 10
    sound = 'raaaaaaaaaar'
