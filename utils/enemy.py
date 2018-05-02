from entity import Entity


class Enemy(Entity):
    def __init__(self, *, health=100, mana=100, damage=20):
        super().__init__(health=health, mana=mana)
        self.__baseDamage = damage

    def get_base_damage(self):
        return self.__baseDamage
