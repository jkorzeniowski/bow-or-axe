class Weapon:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage


class Bow(Weapon):
    def __init__(self):
        super().__init__("Bow", 30)


class Axe(Weapon):
    def __init__(self):
        super().__init__("Axe", 45)


class Character:
    def __init__(self, weapon: Weapon, hp: int):
        self.weapon = weapon
        self.hp = hp
        self.alive = True

    def attack(self, target: 'Character'):
        target.take_damage(self.weapon.damage)

    def take_damage(self, weapon_damage: int):
        if self.alive:
            if self.hp - weapon_damage < 0:
                self.hp = 0
                self.alive = False
            else:
                self.hp -= weapon_damage

    def is_alive(self):
        return self.alive
  

if __name__ == '__main__':
    elf = Character(Bow(), hp=50)
    dwarf = Character(Axe(), hp=80)
    elf.attack(dwarf)
    assert dwarf.is_alive()
    elf.attack(dwarf)
    assert dwarf.is_alive()
    elf.attack(dwarf)
    assert not dwarf.is_alive()
