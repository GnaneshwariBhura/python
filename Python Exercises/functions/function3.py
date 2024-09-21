
n=int(input("Enter the number: ")) 
def print_pattern(n):
    # n=int(input())
    for i in range(n+1):
        print('*'*i)
print_pattern(n)
    

    # create inheritance using animal Dog relation.
# for example, 
#     Animal and Dog both has same habitat so create a method for habitat 

class Animal:
    name="Dog"
    # habit=None
    # def __init__(self,name):
    #     self.name=name
    #     self.habit=habit
    # # def eat(self):
    # #     print("The ",self.name , "Is eating")
    def habitat(self):
        # habit=self.habit
        print(self.name, "is its Barking")
class Dog(Animal):
    def __init__(self):
        pass
    def habitat(self,name):
        super().habitat()
        
a=Dog()
print(a.habitat())
