'''this is going to be a manual test'''

from hero import Hero
from enemy import Enemy
from spell import Spell
from weapon import Weapon
from fight import Fight

h = Hero(name="Genadi", title="The Gopnik")
s = Spell(name="Kwass Molotov", damage=5, manaCost=50, castRange=5)
s1 = Spell(name="Magic spit", damage=10, manaCost=25, castRange=50)
w1 = Weapon(name="Bat", damage=50)
w = Weapon(name="Beer Bottle", damage=25)

h.equip(w)
h.learn(s)
h.coordinates = (0, 5)

e = Enemy()
e.name = "Bad guy"
e.learn(s1)
e.equip(w1)
e.coordinates = (0, 0)


f = Fight(h, e)
f.initialize_fight()
