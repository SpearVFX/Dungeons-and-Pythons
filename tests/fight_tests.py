'''this is going to be a manual test'''

from src.hero import Hero
from src.enemy import Enemy
from src.spell import Spell
from src.weapon import Weapon
from src.fight import Fight
from src.fight_status_bar import FightStatusBar

h = Hero(name="Genadi", title="Gopnik")

s = Spell(name="Kwass Molotov", damage=5, manaCost=10, castRange=7)
s1 = Spell(name="Magic spit", damage=10, manaCost=25, castRange=2)

w = Weapon(name="Beer Bottle", damage=25)
w1 = Weapon(name="Bat", damage=22)

h.equip(w)
h.learn(s)
h.coordinates = (0, 7)

e = Enemy()

e.learn(s1)
e.equip(w1)
e.coordinates = (0, 0)

""" 
f = Fight(h, e,)
f.initialize_fight() """
