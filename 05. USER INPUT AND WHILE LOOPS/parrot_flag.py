prompt = "\nTell me something, and I will repeat it to you."
prompt += "\nEnter your message or type 'quit' to end the program."
prompt += "\nEnter: "

active = True
while active: 
    message = input(prompt)

    if message == 'quit':
        active = False
        print('\nThe End')
    else:
        print('\n' + 'Repeating: ' + message) 