import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class FightStatusBar:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        self.status_string = ""

    def header_string_with_clear_terminal(self):
        cls()
        self.header_string()
        pass

    def header_string(self):
        print('+{0:-^50}+{0:-^50}+'.format(''))
        print('|{:^50}|{:^50}|'.format(self.hero.known_as(), "Enemy"))
        print('+{0:-^50}+{0:-^50}+'.format(''))
        self.health_mana_status_bar()
        pass

    def bar_string(self, stats):
        bar_string = ['', '']
        size = int(stats[0] * 50)
        for x in range(0, size):
            bar_string[0] += "█"

        size = int(stats[1] * 50)
        for y in range(0, size):
            bar_string[1] += "█"

        return(bar_string[0], bar_string[1])

    def get_max_cur_mana_hp(self, e):
        maxHp = e.get_max_health()
        maxMa = e.get_max_mana()

        curHp = e.get_health()
        curMa = e.get_mana()

        return([(curHp, maxHp), (curMa, maxMa)])

    def calculate_ratio(self, e):
        stats = self.get_max_cur_mana_hp(e)

        return (stats[0][0]/stats[0][1], stats[1][0]/stats[1][1])  # cur / max

    def health_mana_status_bar(self):
        hero_bar = self.bar_string(self.calculate_ratio(self.hero))
        enemy_bar = self.bar_string(self.calculate_ratio(self.enemy))
        hero_stats = self.get_max_cur_mana_hp(self.hero)
        h_health_string = f'{hero_stats[0][0]}/{hero_stats[0][1]}'
        h_mana_string = f'{hero_stats[1][0]}/{hero_stats[1][1]}'
        enemy_stats = self.get_max_cur_mana_hp(self.enemy)
        e_health_string = f'{enemy_stats[0][0]}/{enemy_stats[0][1]}'
        e_mana_string = f'{enemy_stats[1][0]}/{enemy_stats[1][1]}'

        print('|\x1b[31m{:<50}\x1b[0m|\x1b[31m{:<50}\x1b[0m|'.format(hero_bar[0], enemy_bar[0]))
        print('|\x1b[31m{:^50}\x1b[0m|\x1b[31m{:^50}\x1b[0m|'.format(h_health_string, e_health_string))
        print('|\x1b[34m{:<50}\x1b[0m|\x1b[34m{:<50}\x1b[0m|'.format(hero_bar[1], enemy_bar[1]))
        print('|\x1b[34m{:^50}\x1b[0m|\x1b[34m{:^50}\x1b[0m|'.format(h_mana_string, e_mana_string))
