# [x] 1 Your class should contain at least one abstract method and one regular method.  
# [x] 2 Create a child class that defines the implementation of its parents abstract method.
# [x] 3 Create an object that utilizes both the parent and child methods.
#----------------------------------------------------------------------

from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ",amount)
#this function is telling us to pass and argument
    @abstractmethod #----------------------------step 1
    def payment(self, amount):
        pass

class DebitCardPayment(car): #-------------------step 2
    #this is defining how to implement the payment function from is parent paySlip class.
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")
