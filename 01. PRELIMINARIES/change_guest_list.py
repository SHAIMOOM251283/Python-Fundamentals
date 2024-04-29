guest = ['Albert', 'Einestine', 'Lee Major']

message = ' you are cordialy invited to grace the event with your presence.'

print(guest[0] + ', ' + message)
print("\n" + guest[1] + ', ' + message)
print("\n" + guest[2] + ', ' + message)

unavailable = 'Einestine'
guest.remove(unavailable)
#del guest[1]

print("\n" + unavailable + " is not avalable for the event.")

print("\n" + str(guest))

guest.insert(1, 'MacGyver')

print("\n" + str(guest))

print("\n" + guest[0] + ', ' + message)
print("\n" + guest[1] + ', ' + message)
print("\n" + guest[2] + ', ' + message)


