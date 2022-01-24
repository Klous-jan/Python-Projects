# [x]Step 1: Each child should have at least two of their own attributes.
# [x]Step 2: The parent class should have at least one method (function).
# [x]Step 3: Both child classes should utilize polymorphism on the parent class method.
# [x]Step 4: Add comments throughout your Python explaining your code.

# Parent class
class User:
    name = "john"
    email = "jdoe@gmail.com"
    password = "pass5678"
    
    # Start of parent method
    def getLoginInfo(self):
        # input lets the user type in command to interact with the script
        entry_name = input("Enter name: ")
        entry_email = input("enter email: ")
        entry_password = input("enter password: ")
        # if the email and password entered match whats saved its good to go and prints the welcome back message.
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(entry_name))
        # if the email and password entered do not patch match it returns the following
        else:
            print("The password or email is incorrect")

# Child class
class Corporate(User):
    base_pay = 35.00
    department = "main office"
    region = "North America"
    boss = "Larry Bossman"
    secret_phrase = "i dont know what to add!"

# same method as User, but it uses secret_phrase instead of password

    # Start of child method
    def getLoginInfo(self):
        entry_name = input("Enter name: ")
        entry_email = input("enter email: ")
        entry_secret_phrase = input("enter secret phrase: ")
        if (entry_email == self.email and entry_secret_phrase == self.secret_phrase):
            print("Welcome back, {}".format(entry_name))
        else:
            print("The secret phrase or email is incorrect") 

# Child class
class Employee(User):
    base_pay = 11.00
    department = "General"
    full_or_part = "Fulltime"
    pin_number = "1234"

# same method as User, but it uses pin instead of password

    # Start of child method
    def getLoginInfo(self):
        entry_name = input("Enter name: ")
        entry_email = input("enter email: ")
        entry_pin_number = input("enter pin: ")
        if (entry_email == self.email and entry_pin_number == self.pin_number):
            print("Welcome back, {}".format(entry_name))
        else:
            print("The pin or email is incorrect")


# calls the methods inside each class for User, Employee, and Corperate
customer = User()
customer.getLoginInfo()
manager = Employee()
manager.getLoginInfo()
lead = Corporate()
lead.getLoginInfo()

if __name__ == "__main__":
    print(customer.getLoginInfo())
    print(manager.getLoginInfo())
    print(lead.getLoginInfo())



















