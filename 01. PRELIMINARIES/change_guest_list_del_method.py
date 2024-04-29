guest = []

guest_input = input('Enter Name of Guest: ')
guest.append(guest_input)

guest_input = input('Enter Name of Guest: ')
guest.append(guest_input)

guest_input = input('Enter Name of Guest: ')
guest.append(guest_input)

print("\n" + str(guest))

message = ' you are cordialy invited to grace the event with your presence.'

print("\n" + guest[0] + ', ' + message)
print("\n" + guest[1] + ', ' + message)
print("\n" + guest[2] + ', ' + message)

print("\n" + guest[1] + " can't make it to the event.")

del guest[1]

print("\n" + str(guest))

guest_input = input("\n" + 'Enter Name of Guest: ')
guest.append(guest_input)

print("\n" + str(guest))

print("\n" + guest[0] + ', ' + message)
print("\n" + guest[1] + ', ' + message)
print("\n" + guest[2] + ', ' + message)

print("\n" + 'The total number of guests are: ' + str(len(guest)))