favorite_number = {
    'tom': [420, 300],
    'bill': [750, 800],
    'alan': [980, 790],
    'aron': [300, 400],
    'nick': [120, 240],
    }

for n, l in sorted(favorite_number.items()):
    print("\n" + n.title() + "'s favorite languages are:")
    for numbers in l:
        print("\t" + str(numbers))