class Weapon:
    def __init__(self, *, name="", damage=0):
        self.__name = name
        self.__damage = damage

    def __str__(self):
        return self.__name

    def get_damage(self):
        return self.__damage