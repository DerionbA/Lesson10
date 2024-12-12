class Employee:

    
 def __init__(self):

    print("EMployee Created")


 def __del__ (self):
    print("Destructor called, Employee deleted.")

obj = Employee()

del obj