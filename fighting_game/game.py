import sys
from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        print("Monster's Turn!!")
        if self.monster.attack():
            print("A {} is attacking!".format(self.monster))
            if input("Dodge? [Y/n] ").lower() != 'n':
                if self.player.dodge():
                    print("Your dodge was successful!")
                    print(self.player)
                else:
                    self.player.hitPoints -=1    #exercise
                    print("You got hit anyway!")
                    print(self.player)
            else:
                self.player.hitPoints -= 1
                print("You lost one hit point!")
                print(self.player)
        else:
            print("The {} isn't attacking.".format(self.monster))

    def player_turn(self):
        print("Your turn")
        action = input("Do you want to [A]ttack, [R]est, or [Q]uit? ").lower()
        if action in 'arq':
            if action == 'a':
                if self.player.attack():
                    print("You attack successfully!")
                    if self.monster.dodge():
                        print("The {} dodged the attack!".format(self.monster))
                    else:
                        if self.player.leveledUp():
                            self.monster.hitPoints -= 2
                        else:
                            self.monster.hitPoints -= 1
                        print("You hit {} with your {}!".format(self.monster, self.player.weapon))
                else:
                    print("Your attack missed.")
            elif action == 'r':
                self.player.rest()
            else:
                print("Bye")
                sys.exit()
        else:
            return player_turn()


    def cleanup(self):
        if self.monster.hitPoints <= 0:
            self.player.experience += self.monster.experience
            print("You killed {}!".format(self.monster))
            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()

        while self.player.hitPoints and (self.monster or self.monsters):
            print('\n'+'='*20)
            print(self.player)
            self.monster_turn()
            print('-'*20)
            self.player_turn()
            self.cleanup()
            print('\n'+'='*20)

            if self.player.hitPoints:
                print("You win!")
            elif self.monsters or self.monster:
                print("You lose!")
            sys.exit()


Game()
