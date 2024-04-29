messages = ['smoke on the water',
            'love will keep us alive', 'fly to the rainbow']
sent_messages = []


def send(messages):
    while messages:
        msg = messages.pop()
        print(f"Printing Messages: {msg}")
        sent_messages.append(msg)


send(messages[:])

# Print the messages list after calling send()
print("\nThe remaining messages:")
print(messages)


def show(sent_messages):
    print("\nThe following messages have been sent:")
    for sent in sent_messages:
        print(sent)


show(sent_messages)
