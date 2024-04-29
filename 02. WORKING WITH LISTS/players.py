players = ['charles', 'martina', 'michael', 'florence', 'eli'] 

print(players[0:3])
print("\n" + str(players[1:4]))
print("\n" + str(players[:4]))
print("\n" + str(players[2:]))
print("\n" + str(players[-3:]))
print("\n" + str(players[::-1]))
print("\n" + str(players[::2]))
print("\n" + str(players[1::2]))
print("\n" + str(players[3:0:-1]))

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print("\n" + str(player.title()))


