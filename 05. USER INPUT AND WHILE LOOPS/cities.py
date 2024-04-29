prompt = "\nPlease enter the name of a city you have visited."
prompt += "\nEnter 'quit' when you are finished."
prompt += "\nEnter: "

while True:
    city = input(prompt)
    if city == 'quit':
        print("\nThe End")
        break
    else:
        print(f"\nI'd love to go to {city.title()}!")
