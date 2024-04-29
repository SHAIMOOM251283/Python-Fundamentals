class Die:

    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        for _ in range(10):
            result = f"{__import__('random').randint(1, self.sides)}"
            print(result)
    
    def increment_die_sides(self, increment):
        self.sides += increment

# Creating a 6-sided die
six_sided_die = Die()
print("\n---6 SIDED DICE---")
six_sided_die.roll_die()

# Creating a 10-sided die
ten_sided_die = Die(sides=10)
print("\n---10 SIDED DICE---")
ten_sided_die.roll_die()

# Creating a 20-sided die
twenty_sided_die = Die(sides=20)
print("\n---20 SIDED DICE---")
twenty_sided_die.roll_die()


