def send(messages, sent_messages):
    while messages:
        msg = messages.pop()
        print(f"Printing Messages: {msg}")
        sent_messages.append(msg)


def show(sent_messages):
    print("\nThe following messages have been sent:")
    for sent in sent_messages:
        print(sent)


messages = ['smoke on the water',
            'love will keep us alive', 'fly to the rainbow']
sent_messages = []

send(messages[:], sent_messages)

print("\nOriginal list:")
print(messages)

show(sent_messages)
