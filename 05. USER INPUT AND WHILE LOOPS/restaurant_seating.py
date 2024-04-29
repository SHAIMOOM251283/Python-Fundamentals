prompt = 'Please state the number of guests.'
prompt += '\nEnter: '

guests = int(input(prompt))

if guests > 8:
    print("\nSorry, you'll have to wait for a table.")
else:
    print("\nYour desired table is ready.")