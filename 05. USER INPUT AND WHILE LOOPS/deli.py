sandwich_orders = ['tuna', 'beef', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"Preparing {current_order.title()} sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been made:")
for completed_order in finished_sandwiches:
    print(f"{completed_order.title()} sandwich")