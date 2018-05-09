from src.entity import Entity


class Enemy(Entity):
    def __init__(self, *, name=None,health=100, mana=100, damage=20):
        super().__init__(name=name,health=health, mana=mana)
        self.__baseDamage = damage

    def get_base_damage(self):
        return self.__baseDamage
    
    def __str__(self):
        return f'({super().__str__()}, damage={self.__baseDamage})'
    def __repr__(self):
        return self.__str__()
