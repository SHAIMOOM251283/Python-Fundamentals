def show_messages(messages):
    """ Messages """
    for msg in messages:
        print(f"\n{msg.title()}")


messages = ['smoke on the water',
            'love will keep us alive', 'fly to the rainbow']

print("\n--- Messages ---")
show_messages(messages)
