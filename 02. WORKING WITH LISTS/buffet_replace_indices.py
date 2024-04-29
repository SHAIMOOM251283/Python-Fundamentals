menu = ('sushi', 'teriyaki chicken', 'sake soup', 'tempura', 'gyoza')
print('Original Menu:')
for item in menu:
    print(item.title())

print("\n")

indices_to_replace = [menu.index(item)
                      for item in ['teriyaki chicken', 'sake soup']]
revised_menu = (
    menu[:indices_to_replace[0]] + ('ramen',) +
    menu[indices_to_replace[0]+1:indices_to_replace[1]] + ('pho',) +
    menu[indices_to_replace[1]+1:]
)
print("Revised Menu:")
for item in revised_menu:
    print(item.title())
