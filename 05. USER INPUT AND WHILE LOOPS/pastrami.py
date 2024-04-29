sandwich_orders = ['tuna', 'pastrami', 'beef', 'pastrami', 'chicken', 'pastrami']
finished_sandwiches = []

out_of_stock = input('Enter Item: ')

print(f"\n{out_of_stock.title()} is not available.")

while out_of_stock in sandwich_orders:
    sandwich_orders.remove(out_of_stock)
    
print(f"\nAvailable sandwiches: {[sandwich.title() for sandwich in sandwich_orders]}")

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"\nPreparing {current_order.title()} sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been made:")
for completed_order in finished_sandwiches:
    print(f"{completed_order.title()} sandwich")