class Parent:
    def __init__(self):
        print("This is the parent class")
    def parentFunc(self):
        print("This is the parent func")

#Child inherits Parent
class Child(Parent):
    def __init__(self):
        print("This is the child class")
    def childFunc(self):
        print("This is the child func")

c = Child()
c.childFunc()
c.parentFunc()
