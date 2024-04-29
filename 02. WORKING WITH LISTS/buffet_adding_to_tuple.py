menu = ('sushi', 'teriyaki chicken', 'sake soup', 'tempura', 'gyoza')
print('Original Menu:')
for item in menu:
    print(item.title())

print("\n")

revised_menu = menu + ('thai soup', 'chicken fry')
print('Modified Menu:')
for item in revised_menu:
    print(item.title())

print("\n")

index_to_replace = menu.index('teriyaki chicken')
revised_menu = menu[:index_to_replace] + ('ramen',) + menu[index_to_replace+1:]
print('Revised Menu:')
for item in revised_menu:
    print(item.title())
