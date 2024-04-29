players = []

while True:
    name = input("\nEnter Name: ").title()
    players.append(name)

    repeat = input("\nDo you want to enter more names? (yes/no): ").lower()

    if repeat != 'yes':
        break

print(f"\nFIrst Up: {__import__('random').choice(players)}")

print("\n")