from hero import Hero
from enemy import Enemy
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class FightStatusBar:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        self.status_string = ""

    def header_string(self):
        cls()
        print('+{0:-^50}+{0:-^50}+'.format(''))
        print('|{:^50}|{:^50}|'.format(self.hero.known_as(), "Enemy"))
        print('+{0:-^50}+{0:-^50}+'.format(''))
        self.health_mana_status_bar()
        pass

    def print_bar(self, stats):
        bar_string = ['', '']
        size = int(stats[0] * 50)
        for x in range(0, size):
            bar_string[0] += "█"

        size = int(stats[1] * 50)
        for y in range(0, size):
            bar_string[1] += "█"

        return(bar_string[0], bar_string[1])

    def calculate_ratio(self, e):
        maxHp = e.get_max_health()
        maxMa = e.get_max_mana()

        curHp = e.get_health()
        curMa = e.get_mana()

        return (curHp/maxHp, curMa/maxMa)

    def health_mana_status_bar(self):
        heroStats = self.print_bar(self.calculate_ratio(self.hero))
        enemyStats = self.print_bar(self.calculate_ratio(self.enemy))
        print('|\x1b[31m{:<50}\x1b[0m|\x1b[31m{:<50}\x1b[0m|'.format(heroStats[0], enemyStats[0]))
        print('|\x1b[34m{:<50}\x1b[0m|\x1b[34m{:<50}\x1b[0m|'.format(heroStats[1], enemyStats[1]))
