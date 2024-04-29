start = int(input("Enter the start of the range: "))
stop = int(input("Enter the end of the range: "))
step = int(input("Enter the step of the range: "))

numbers = [value for value in range(start, stop, step)]

min_number = min(numbers)
max_number = max(numbers)
sum_numbers = sum(numbers)

print("Minimum number:", min_number)
print("Maximum number:", max_number)
print("Sum of numbers:", sum_numbers)
