unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


def print_models(unprinted):
    while unprinted:
        current_design = unprinted.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


print_models(unprinted_designs[:])

print("\nThe remaining models:")
print(unprinted_designs)

def show_completed_models(completed):
    print("\nThe following models have been printed:")
    for model in completed:
        print(model)


show_completed_models(completed_models)
