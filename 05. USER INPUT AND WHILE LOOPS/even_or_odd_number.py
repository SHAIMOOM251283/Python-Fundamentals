prompt = "Enter a number, and I'll tell you if it's even or odd."
prompt += '\nEnter: '

number = int(input(prompt))

if number % 2 == 0:
    print('\nThe number ' + str(number) + ' is even.')
else:
    print('\nThe number ' + str(number) + ' is odd.')
