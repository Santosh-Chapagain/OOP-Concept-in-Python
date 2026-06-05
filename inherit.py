# #Super inheritance

# class Animal:
#     def __init__(self, animal):
#         # print(id(self))
#         self.animal= animal
#     def info1(self):
#         print(f"{self.animal} are dangerous")

# class Dog(Animal):
#     def info2(self):
#         # print(id(self))
#         print(f"{self.animal} barks")

# a1 = Animal("Lion")
# # print(id(a1))
# # a1.info1()

# a2= Dog("Dog")
# print(id(a2))
# a2.info2()
# a2.info1()


# Super keyword
class Sidetalk_master:
    def __init__(self, name):
        self.name= name

    def disturber(self):
        print(f"{self.name} is disturbing whole class.")

class Sidetalk_child(Sidetalk_master):
    def __init__(self, name, listner):
        super().__init__(name)
        self.listner = listner
    
    def talk(self):
        super().disturber()
        print(f"{self.name} is talking with {self.listner}")

s1= Sidetalk_master("Dipesh")
s2= Sidetalk_child("Dipesh", "Santosh")

s2.talk()