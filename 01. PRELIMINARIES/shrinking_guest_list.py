guest = []

guest_input = input('Enter Name of Guest: ')
guest.append(guest_input)

guest_input = input("\n" + 'Enter Name of Guest: ')
guest.append(guest_input)

guest_input = input("\n" + 'Enter Name of Guest: ')
guest.append(guest_input)

print("\n" + str(guest))

message = 'you are cordialy invited to grace the event with your presence.'

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

message = 'I am delighted to inform you that I found a bigger dinner table and the party just got bigger.'

print("\n" + guest[0] + ', ' + message)
print("\n" + guest[1] + ', ' + message)
print("\n" + guest[2] + ', ' + message)

guest_input = input("\n" + 'Enter Name of Guest: ')
guest.insert(0, guest_input)

guest_input = input("\n" + 'Enter Name of Guest: ')
guest.insert(2, guest_input)

guest_input = input("\n" + 'Enter Name of Guest: ')
guest.append(guest_input)

print("\n" + str(guest))

message = 'you are cordialy invited to grace the event with your presence.'

print("\n" + guest[0] + ', ' + message)
print("\n" + guest[1] + ', ' + message)
print("\n" + guest[2] + ', ' + message)
print("\n" + guest[3] + ', ' + message)
print("\n" + guest[4] + ', ' + message)
print("\n" + guest[5] + ', ' + message)

print("\n" + 'Owing to unavalability of the larger table, only two guests can be invited in the present capacity.')

message = 'please accept my sincere apologies for being compelled to cancel your invitation.'

guest_removed = guest.pop()
print("\n" + guest_removed + ', ' + message)

guest_removed = guest.pop()
print("\n" + guest_removed + ', ' + message)

guest_removed = guest.pop()
print("\n" + guest_removed + ', ' + message )

guest_removed = guest.pop()
print("\n" + guest_removed + ', ' + message )

print("\n" + str(guest))

message = 'you are sincerely requested to to accept the invitation to grace the event with your presence.'

print("\n" + guest[0] + ', ' + message)
print("\n" + guest[1] + ', ' + message)

del guest[1]
print("\n" + str(guest))

del guest[0]
print("\n" + str(guest))








