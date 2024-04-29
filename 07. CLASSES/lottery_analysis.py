import random

lottery =(1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 'A', 'B', 'C', 'D', 'E')
my_ticket = (17, 25, 'A', 'B')


num_attempts = 0
while True:
    num_attempts += 1
    
    #drawn_ticket = random.sample(lottery, 4)
    #if drawn_ticket == list(my_ticket):
    
    drawn_ticket = [random.choice(lottery) for _ in range(4)]
    if drawn_ticket == list(my_ticket):
        print("Congratulations! You've won!")
        break

print(f"It took {num_attempts} attempts to win with your ticket.")





