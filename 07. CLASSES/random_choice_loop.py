from random import choice

players = []

while True:
    name = input("\nEnter Name (Enter 'done' to finish): ").title()
    
    if name.lower() == 'done':
        break
    else:
        players.append(name)

print("\n---Names---")
for i in range(10):
    i = choice(players).title()
    print(i)