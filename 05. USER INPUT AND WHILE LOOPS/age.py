prompt = '\nHow old are you?'
prompt += '\nEnter: '

active = True 
while active:
    age_input = input(prompt)

    if age_input.lower() == 'quit':
        active = False
        print('\nThe End!')

    else:
        try:
            age = int(age_input)
            print(f"\nYou are {str(age)} years old.")
        except:
            print("\nPlese enter a valid age or 'quit'.")
            continue
        
    
