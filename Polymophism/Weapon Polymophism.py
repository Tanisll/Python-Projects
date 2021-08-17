class Weapon:
    damage = "1d6"
    reach = '5ft'
    weight = '2 lb.'
    cost = 0
    dmg_type = 'piercing'

    def Attack(self):
        X = "Swing your weapon at a target within reach and make an attack roll against their AC rating."
        Y = "Thrust your weapon at a target within reach and make an attack roll against their AC rating."
        print(X)

class Dagger(Weapon):
    damage = '1d4'
    weight = '1 lb.'
    cost = '2 gp'
    color = 'Black'
    material = 'Steel'

    def Attack(self):
        X = "Swing your weapon at a target within reach and make an attack roll against their AC rating."
        Y = "Thrust your weapon at a target within reach and make an attack roll against their AC rating."
        print(Y)

class Warhammer(Weapon):
    damage = '1d8'
    weight = '3 lb.'
    cost = '15 gp'
    dmg_type = 'bludgeoning'
    style = 'Orcish'
    force = 'Knockback 10 ft.'

    def Attack(self):
        X = "Swing your weapon at a target within reach and make an attack roll against their AC rating."
        Y = "Thrust your weapon at a target within reach and make an attack roll against their AC rating."
        print(X)


if __name__ == "__main__":
