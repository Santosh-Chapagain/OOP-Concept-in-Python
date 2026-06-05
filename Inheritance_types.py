# Multi-Level inheritance
# class Grandparents:
#     def __init__(self, name):
#         self.name= name 
    
#     def tell_story(self):
#         print(f"{self.name} tells story")

# class Parents(Grandparents):
#     def working(self):
#         print(f"{self.name} is working")

# class Child(Parents):
#     def reading(self):
#         print(f"{self.name} is reading")

# c1= Child("Ramesh")
# c1.tell_story()
# c1.working()
# c1.reading()

# ------------------------------------------------------------------------------

# Hierarchical Inheritance => Multiple child with single parent 


# class Parents:
#     def __init__(self, name):
#         self.name = name

#     def tell_story(self):
#         print(f"{self.name} tells story")


# class Child1(Parents):
#     def working(self):
#         print(f"{self.name} is working")


# class Child2(Parents):
#     def reading(self):
#         print(f"{self.name} is reading")


# c1 = Child1("Ramesh")
# c2 = Child2("Harish")
# c1.tell_story()
# c2.tell_story()
# c1.working()
# c2.reading()

# ----------------------------------------------------------------------------


# Hybrid Inheritance =>
#     Hierarchical inheritance(B and C inherit from A)
#     Multiple inheritance(D inherits from both B and C) 
class A:
    def show_a(self):
        print("Class A")


class B(A):
    def show_b(self):
        print("Class B")


class C(A):
    def show_c(self):
        print("Class C")


class D(B, C):
    def show_d(self):
        print("Class D")


obj = D()

obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()

    #   A
    #  / \
    # B   C
    #  \ /
    #   D