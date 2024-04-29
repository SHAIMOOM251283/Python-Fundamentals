#numbers = [value**2 for value in range(1, 11, 1)]
#print(numbers)


start = int(input("Enter the start of the range: "))
stop = int(input("Enter the end of the range: "))
step = int(input("Enter the step of the range: "))

expression = input('Enter the expression to calculate each number: ')

numbers = [value**int(expression) for value in range(start, stop, step)]

print(numbers)
