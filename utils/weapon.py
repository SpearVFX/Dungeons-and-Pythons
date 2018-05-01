class Weapon:
    def __init__(self, *, name="", damage=0):
        self.__name = name
        self.__damage = damage

    def __str__(self):
        return f'{self.__name}, damage = {self.__damage}.'

    def get_damage(self):
        return self.__damage