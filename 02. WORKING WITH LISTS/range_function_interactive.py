numbers = []

start = int(input("Enter the start of the range: "))
stop = int(input("Enter the end of the range: "))
step = int(input("Enter the step of the range: "))

expression = input('Enter the expression to calculate each number: ')

for value in range(start, stop, step):
    #number = value**int(expression)
    #numbers.append(number)
    numbers.append(value**int(expression))

print(numbers)
