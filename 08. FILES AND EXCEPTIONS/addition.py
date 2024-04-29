while True:
    try:
        answer = int(input("\nFirst Number: ")) + int(input("Second Number: "))
    except(ValueError):
        print("Enter Integer Only!")
    else:
        print("The answer is",answer)
    
    repeat = input("\nDo you want to add another set of numbers (yes/no)? ")
    if repeat.lower() != 'yes':
        print("\nProgram Terminated!")
        break
    
    




