items = []

items_input = input('Enter Item: ')
items.append(items_input)

items_input = input('Enter Item: ')
items.append(items_input)

items_input = input('Enter Item: ')
items.append(items_input)

items_input = input('Enter Item: ')
items.append(items_input)

items_input = input('Enter Item: ')
items.append(items_input)

print("\n" + str(items))
print(items[0])
print(items[4].title())
print(items[2].upper())
print(items[2])
print(items[3])
print(items[-1])
print(items[-2].title())
print(items[-3].upper())

favourite = input("\n" + str('Item category: '))
message = 'My favourite ' + favourite + ' is ' + items[0].title() + '.'
print("\n" + str(message))

items[0] = input("\n" + str('Replace item at index 0 with: '))
print("\n" + str(items))

items.insert(0, input("\n" + str('Insert item at index 0: ')))
print("\n" + str(items))

items.insert(1, input("\n" + str('Insert item at index 1: ')))
print("\n" + str(items))

del items[0]
print("\n" + str(items))

del items[1]
print("\n" + str(items))

print("\n" + 'Popped item: ' + str(items.pop()))

print("\n" + str(items))

print("\n" + 'The popped item from the list is ' + str(items.pop(1)) + '.')

print("\n" + str(items))

new_items = items.pop()
print("\n" + 'The popped item is ' + new_items.title() + '.')

latest_items = items.pop(1)
print("\n" + 'The item popped from the list is ' + latest_items.title() + '.')

print("\n" + str(items))

items_input = input("\n" + 'Enter Item: ')
items.append(items_input)

items_input = input('Enter Item: ')
items.append(items_input)

items_input = input('Enter Item: ')
items.append(items_input)

print("\n" + str(items))

print("\n" + str(sorted(items)))

print("\n" + str(sorted(items, reverse=True)))

print("\n" + str(items))

items.reverse()
print("\n" + str(items))

print("\n" + 'The length of the list is: ' + str(len(items)))

items_for_removal = ['burger', 'pizza', 'hot dog', 'pasta']
print("\n" + str(items_for_removal))
not_favourite = 'hot dog'
items_for_removal.remove(not_favourite)
print("\n" + str(items_for_removal))
print("\n" + not_favourite.title() + ' is not my favourite.')


















