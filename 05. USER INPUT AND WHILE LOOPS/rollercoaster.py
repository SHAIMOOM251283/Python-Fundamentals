prompt = 'How tall are you, in inches?'
prompt += '\nEnter: '

height = int(input(prompt))

if height > 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're taller.")