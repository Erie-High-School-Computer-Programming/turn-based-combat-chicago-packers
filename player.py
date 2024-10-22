class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hp = 100



    def attack(self, move, target):
        """This method should allow the character to attack another character using the 
        selected move. The move should deal damage to the target character"""
        target.hp -= move

    move_list = {"Punch": {"damage": 10,
                           "accuracy": 75}
                 }

    import random
    if random.randint(0, 100) < move_list["Punch"]["accuracy"]:
        Ernie.hp -= move_list["Punch"]["damage"]
        print("Ernie was Punched")
    else:
        print("Attack missed")

    def display_stats(self):
        """This method should display the current health of the character"""
        


p1 = Player("Peter Griffin", 100)
p2 = Player("Ernie The Giant Chicken", 100)

print(p2.hp)
p1.attack(30, p2)
print(p2.hp)