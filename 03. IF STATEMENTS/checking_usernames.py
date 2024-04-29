current_users = ['tom', 'alan', 'Long', 'John', 'SILVER']

new_users = []

user = input('Enter Name: ')
if user:
    new_users.append(user)

user = input('Enter Name: ')
if user:
    new_users.append(user)

user = input('Enter Name: ')
if user:
    new_users.append(user)

user = input('Enter Name: ')
if user:
    new_users.append(user)

user = input('Enter Name: ')
if user:
    new_users.append(user)

print('\n')

if new_users:
    for user in new_users:
        if user.lower() in [name.lower() for name in current_users]:
            print('Enter a new username.')
        else:
            print(user + ' is available.')
else:
    print('We need to find some users!!!')