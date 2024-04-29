start = int(input("Enter the start of the range: "))
stop = int(input("Enter the end of the range: "))
step = int(input("Enter the step of the range: "))

numbers = [value for value in range(start, stop, step)]

print(numbers)

#   The first value represents the computation or operation to be performed on each item in the iterable.
#   The second value is a variable that represents each individual element or value in the iterable.

