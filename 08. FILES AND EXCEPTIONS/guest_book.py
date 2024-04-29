from pathlib import Path

print("---Guest List---")
guest_list = []

while True:
    try:
        first_name = input("\nEnter First Name: ").title()
        last_name = input("Enter Last Name: ").title()
        guest_list.append(f"{first_name} {last_name}")

        repeat = input("\nDo you want to enter more names? (yes/no): ").lower()

        if repeat != 'yes':
            break

    except(ValueError, KeyboardInterrupt):
        print("\nInvalid input or keyboard interrupt. Please try again.")

print("\n---LIST OF NAMES---")
for names in guest_list:
    print(names)

content = "GUEST BOOK\n\n" + '\n'.join(guest_list)

Path('guest_book.txt').write_text('\n'.join(content.splitlines()))

print("\nGuest Book created!")

