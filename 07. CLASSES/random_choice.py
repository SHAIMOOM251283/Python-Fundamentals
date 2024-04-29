from random import choice

players = ['charles', 'martina', 'michael', 'florence', 'eli']

first_up = choice(players).title()

print(first_up)
 
for i in range(10):
    i = f"FIrst Up: {__import__('random').choice(['charles', 'martina', 'michael', 'florence', 'eli']).title()}"
    print(i)

print(f"FIrst Up: {__import__('random').choice(['charles', 'martina', 'michael', 'florence', 'eli']).title()}")