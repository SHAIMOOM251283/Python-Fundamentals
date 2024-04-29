guest = []

user_input = input('Enter name of Guest: ')
guest.append(user_input)

user_input = input('Enter name of Guest: ')
guest.append(user_input)

user_input = input('Enter name of Guest: ')
guest.append(user_input)

print(guest)

message1 = input('Enter Message: ')
message2 = input('Enter Message: ')
message3 = input('Enter Message: ')

print(guest[0] + ', ' + message1)

print(guest[1] + ', ' + message2) 

print(guest[2] + ', ' + message3)

print(len(guest))