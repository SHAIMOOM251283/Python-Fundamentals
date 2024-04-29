age = []

user_input = int(input('Enter Age: '))
age.append(user_input)

if age[0] < 2:
    print('You are a baby.')

elif age[0] < 4:
    print('You are a toddler.')

elif age[0] <13:
    print('You are a kid.')

elif age[0] < 20:
    print('You are a teenager.')

elif age[0] < 65:
    print('You are an adult.')

else:
    print('You are an elder.')

