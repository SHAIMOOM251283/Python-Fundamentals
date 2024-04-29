#from random import randint
#print(f"The lucky number is: {randint(1, 6)}")
#print(f"The lucky number is: {__import__('random').randint(1, 6)}")

print("\n---6 SIDED DICE---")
for i in range(10):
    i = f"{__import__('random').randint(1, 6)}"
    print(i)

print("\n---10 SIDED DICE---")
for i in range(10):
    i = f"{__import__('random').randint(1, 10)}"
    print(i)

print("\n---20 SIDED DICE---")
for i in range(10):
    i = f"{__import__('random').randint(1, 20)}"
    print(i)