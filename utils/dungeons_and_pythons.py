import dungeon
import hero

treasure_map = 'dungeon_maps/test_maps/treasure_map/'


def main():

    dummyDung = dungeon.Dungeon(fileDir=treasure_map)
    dummyHero = hero.Hero()
    dummyDung.spawn(hero=dummyHero)
    dummyDung.print_map()
    dummyDung.move_hero(direction='down')
    dummyDung.print_map()
    print(dummyDung.get_hero().get_weapon())
    print(dummyDung.get_hero().get_spell())


if __name__ == '__main__':
    main()
