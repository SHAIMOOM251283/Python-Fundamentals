prompt = "\nPlease enter the name of your favorite pizza topping."
prompt += "\nEnter 'quit' when you are finished."
prompt += "\nEnter: "

while True:
    pizza = input(prompt)
    if pizza == 'quit':
        print("\nYour pizza is ready.")
        break
    else:
        print(f"\nAdding {pizza.title()} to your pizza.")