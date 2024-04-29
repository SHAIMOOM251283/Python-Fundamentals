magicians = ['alice', 'david', 'carolina']

message1 = 'that was a great trick!'
message2 = "I can't wit to see you next trick, "
message3 = 'Thank you everyone. That was a great show!'

for magician in magicians:
    print("\n" + str(magician.title()) + ', ' + message1)
    #print(magician.title() + ', ' + message1 + "\n")
    print(message2 + magician.title() + ".\n")
    #print("\n" + message2 + magician.title() + '.')

print(message3)
