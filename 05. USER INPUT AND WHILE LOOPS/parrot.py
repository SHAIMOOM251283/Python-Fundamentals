prompt = "\nTell me something, and I will repeat it to you."
prompt += "\nEnter your message or type 'quit' to end the program."
prompt += "\nEnter: "

message = ""

while message != 'quit':
    message = input(prompt)
    if message == 'quit':
        print("\nThe End")
    else:
        print("\n" + "Repeating: " + message)

