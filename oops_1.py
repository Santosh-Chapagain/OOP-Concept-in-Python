class Employee:
    # special method/ magic method / dunder_method -constructor
    def __init__(self):
        self.id= 123
        self.salary= 100000
        self.designation= "MLE"

    def travel(self, destination):
        print(f"Employee is travelling to: {destination}")

# creating object 
e = Employee()
print(e.salary)
e.travel("Canada")