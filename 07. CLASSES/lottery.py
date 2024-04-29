lottery = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 'A', 'B', 'C', 'D', 'E']

print("\nThe Lucky Winners are:")
for _ in range(4):    
    result = f"{__import__('random').choice(lottery)}"
    print(f"Congratulations! The ticket {result} wins a prize!")
