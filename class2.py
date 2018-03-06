class mission_1:

    def __init__(self, name,weapon,code):
        self.name = name
        self.weapon = weapon
        self.strength = 100
        self.code = code
        self.damage = 20

    def mission(self, soldier):
        soldier.strength =  soldier.strength - self.damage
        return soldier.strength


one = mission_1("girish", 'smg', 1656)
two = mission_1("pavan", "mag", 1657)

print(one.strength)
print("mission 1")
print("current strenth: %d"  %two.mission(one))
