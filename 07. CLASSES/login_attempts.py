class User:
    """Simulating login"""

    def __init__(self, first_name, last_name, username, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.login_attempts = login_attempts

    def describe_user(self):
        """Return a formatted description of user."""
        description = f"First Name: {self.first_name}\nLast Name: {self.last_name}\nUsername: {self.username}"
        return description
    
    def logins(self):
        """Print a statement showing the number of logins."""
        if self.login_attempts == 1:
            print(f"{self.username} has logged in {self.login_attempts} time.")
        else:
            print(f"{self.username} has logged in {self.login_attempts} times.") 
        
    def update_logins(self, attempts):
        """
        Set the number of login attempts.
        Reject the change if the number is less than original login attempts.  
        """
        if attempts >= self.login_attempts:
            self.login_attempts = attempts
        else:
            print("Number of attempts cannot be less than the original number of attempts.")
            while attempts < self.login_attempts:
                attempts = int(input("Please enter a number greater than or equal to the original number of attempts: "))
            self.login_attempts = attempts

    def increment_login_attempts(self, increment):
        """Increment login attempts."""
        if increment >= 0:
            self.login_attempts +=increment
        else:
            print("Login attempts cannot be decreased!")
    
    def reset_login_attempts(self):
        """Reset the number of logins."""
        self.login_attempts = 0
        print(f"Login attempts have been reset to {self.login_attempts}.")
    
users = []

while True:
    first_name = input("\nEnter First Name: ").title()
    last_name = input("Enter Last Name: ").title()
    username = input("Enter Username: ").upper()
    login_attempts = int(input("Enter the number of login attempts: "))
    user_info = User(first_name, last_name, username, login_attempts)
    users.append(user_info)

    repeat = input("\nDo you want to add another user? (yes/no): ")
    if repeat.lower() != 'yes':
        break

print("\n---- User Logins ----")
for user in users:
    print("\n")
    
    print(user.describe_user())

    user.logins()

    new_logins = int(input("Enter new login attempts: "))
    user.update_logins(new_logins)

    user.logins()

    increment_logins = int(input("Increment login attempts: "))
    user.increment_login_attempts(increment_logins)

    user.logins()

    increment_logins = int(input("Increment login attempts: "))
    user.increment_login_attempts(increment_logins)    

    user.logins()

    user.reset_login_attempts()

    user.logins()



    


