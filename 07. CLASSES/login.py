class User:
    """Simulating login"""

    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        """Return a formatted description of user."""
        description = f"First Name: {(self.first_name).title()}\nLast Name: {(self.last_name).title()}\nUsername: {self.username}"
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
    
user_info = User('Jack', 'Daniels', 'Captain Morgan')

print(f"Initial value of login_attempts: {user_info.login_attempts}")

print(user_info.describe_user())

user_info.update_logins(20)
user_info.logins()

user_info.update_logins(10)
user_info.logins()

user_info.increment_login_attempts(40)
user_info.logins()

user_info.reset_login_attempts()


