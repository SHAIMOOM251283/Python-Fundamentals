import random

lottery = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 'A', 'B', 'C', 'D', 'E']

my_ticket = [1, 13, 25, 'A']  # Example ticket, you can change it to your preferred numbers


print("\nYour Ticket Numbers:")
print(my_ticket)

print("\nSimulating the Lottery Draw:")
num_attempts = 0

while True:
    num_attempts += 1
    drawn_ticket = [random.choice(lottery) for _ in range(4)]
    #drawn_ticket = random.sample(lottery, 4)
    #print(f"\nAttempt {num_attempts}: {drawn_ticket}")
    if drawn_ticket == my_ticket:
        print(f"\nCongratulations! Your ticket {my_ticket} wins the prize!")
        print(f"It took {num_attempts} attempts to win.")
        break
