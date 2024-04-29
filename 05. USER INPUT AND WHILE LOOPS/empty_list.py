sandwiches = []
finished_sandwiches = []

while True:
    sandwich_name = input('\nEnter Name of Sandwich: ').title()
    sandwiches.append(sandwich_name)

    repeat = input("\nDo you want to enter more items? (yes/no): ").lower()

    if repeat != 'yes':
        break

print(f"\nSandwiches: {[sandwich.title() for sandwich in sandwiches]}")

out_of_stock = input('\nEnter Unavailable Item: ').title()

print(f"\n{out_of_stock} is not available.")

while out_of_stock in sandwiches:
    sandwiches.remove(out_of_stock)
    
print(f"\nAvailable sandwiches: {[sandwich.title() for sandwich in sandwiches]}")

while sandwiches:
    current_order = sandwiches.pop()
    print(f"\nPreparing {current_order.title()} sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been made:")
for completed_order in finished_sandwiches:
    print(f"{completed_order.title()} sandwich")
                           