from src.dungeon import Dungeon
from src.hero import Hero
from src.enemy import Enemy
from src.spell import Spell
from src.weapon import Weapon
from src.fight_status_bar import FightStatusBar, cls

def main():
    dungeon = Dungeon()
    hero = Hero(name='Gandalf', title='Wise', health=100, mana=200, mana_regeneration_rate=10)
    spell = Spell(name='You shall not pass', damage=15, manaCost=20,castRange=2)
    weapon = Weapon(name='Smoke Pipe', damage=5)
    hero.equip(weapon=weapon)
    hero.learn(spell=spell)
    
    command = ''
    dungeon.spawn(hero=hero)
    while True:
        dungeon.print_map()
        command = input('Input a command:\n')

        if  (command == 'left' or 
            command == 'right' or
            command == 'up' or
            command == 'down'):
            
            dungeon.move_hero(direction=command)
        elif command == 'shoot':
            dungeon.shoot_blindly()

        cls()
    pass

if __name__ == "__main__":
    main()