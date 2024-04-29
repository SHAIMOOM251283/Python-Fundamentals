name = 'WHat is your name?'
name += '\nEnter: '
age = 'How old are you?'
age += '\nEnter: '

output_name = input(name)
output_age = input(age)

print(f"\n{output_name.title()}, you are {output_age} years old.")

age = int(output_age)
print(age >= 18)