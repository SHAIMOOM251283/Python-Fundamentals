from pathlib import Path

print("---PRINT INVITATION---")
name = input("\nEnter Name: ").title()

contents = f"Dear {name},\n\n"
contents += "You are codrially invited to grace the occasion with your presence.\n\n"
contents += "Thank you.\n"

Path('guest_invitation.txt').write_text(contents)

print("\nInvitation Printed.")

