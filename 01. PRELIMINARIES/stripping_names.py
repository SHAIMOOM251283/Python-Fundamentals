# Storing the name with whitespace characters
name = "\t \n John Doe \n \t"

# Printing the name with whitespace
print("Name with whitespace:")
print(name)

# Stripping whitespace using lstrip(), rstrip(), and strip() functions
print("\nStripped using lstrip():")
print(name.lstrip())

print("\nStripped using rstrip():")
print(name.rstrip())

print("\nStripped using strip():")
print(name.strip())
