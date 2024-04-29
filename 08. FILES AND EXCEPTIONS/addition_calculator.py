print(('addition of two numbers').upper())
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        print("\nProgram Terminated!")
        break
    
    second_number = input("Second number: ")
    if second_number == 'q':
        print("Program Terminated!")
        break
    
    try:
        answer = int(first_number) + int(second_number)   
    except(ValueError):
        print("Enter Integers Only!")
    else:
        print(answer)