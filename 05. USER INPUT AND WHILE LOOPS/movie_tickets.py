prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished."
prompt += "\nEnter: "

while True:
    age_input = input(prompt)
    if age_input.lower() == 'quit':
        print("\nThank You!")
        break
    
    try:
        age = int(age_input)
    except:
        print("\nPlease enter a valid age or quit.")
        continue
    
    if age < 3:
        print("\nFree Entry!")
    elif age < 12:
        print("\nTicket price $10.")
    else:
        print("\nTicket price $15.")
    