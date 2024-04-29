usernames = []

user = input('Enter Name: ')
if user:
    usernames.append(user)

user = input('Enter Name: ')
if user:
    usernames.append(user)

user = input('Enter Name: ')
if user:
    usernames.append(user)

user = input('Enter Name: ')
if user:
    usernames.append(user)

user = input('Enter Name: ')
if user:
    usernames.append(user)

print('\n')

if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hello admin!')
        else:
            print('Greetings, ' + user + '.')
else:
    print('We need to find some users.')


