#from user_function import *
#from user_function import build_profile
#import user_function
#from user_function import build_profile as bp
import user_function as u

user_profile = {}

while True:
    print("Enter user information (or type 'done' to finish):")
    key = input("Enter key: ")
    if key.lower() == 'done':
        break
    value = input("Enter value: ")
    user_profile[key] = value

#user_profile = build_profile(**user_profile)
#user_profile = user_function.build_profile(**user_profile) 
#user_profile = bp(**user_profile)
user_profile = u.build_profile(**user_profile)

print("User profile:")
print(user_profile)