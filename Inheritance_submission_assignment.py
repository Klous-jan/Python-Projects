# this is the parent class, each child connected to this parent will
# have the same properties; "name email, password".
class user:
    name = 'no name provided'
    email = ' '
    password = '1234567890'

# this is the first child class, it has its own properties and also
# has the properties of the parent class "user".
class Employee(user):
    base_pay = 11.00
    department = 'main floor'

# this is the second child class, it has its own properties and also
# has the properties of the parent class "user" but does not link to
# the first child class.
class Customer(user):
    mailing_address = ''
    mailing_list = True
