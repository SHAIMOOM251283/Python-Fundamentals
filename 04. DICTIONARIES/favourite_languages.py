favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite language is " + 
      favorite_languages['sarah'].title() + 
      ".")

for n, l in favorite_languages.items():
    print("\n" + n.title() + "'s favorite language is " + l.title() + '.')


friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print('\n' + name.title())
    if name in friends:
        print('Hi ' + name.title() + 
              ', I see your favrite language is ' + 
              favorite_languages[name].title() + "!")
    
if 'erin' not in favorite_languages.keys():
    print('\nErin, please take our poll!') 

for name in sorted(favorite_languages.keys()):
    print('\n' + name.title() + ", thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
for language in sorted(favorite_languages.values()):
    print(language.title())

print("\nThe following languages have been mentioned:")
for l in sorted(set(favorite_languages.values())):
    print(l.title())



