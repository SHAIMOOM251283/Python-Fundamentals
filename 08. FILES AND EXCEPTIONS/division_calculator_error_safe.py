print(("Give me two numbers, and I'll divide them.").upper())
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
        answer = int(first_number) / int(second_number)
    except(ZeroDivisionError):
        print("A number cannot be divided by zero!")
    else:    
        print(answer)

print("\n")
