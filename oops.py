'''#4 pillars of oops
# Encapsulation:
#access modifiers
class A:
    def __init__(self,name,age,gender):
#constructor
        self.__name=name#private variabel can be accesed inside of same class which defines with__
        self._age=age#protected variable can be accessed inside if same class and its child class which defines with_
        self.gender=gender#public variable can be accessed inside of same class and outside of all classes which defines with no prefix
    def display(self):
        print(self.__name)
        print(self._age)
        print(self.gender)
    def setAge(self,age):
        self._age=age
    def getAge(self):
        return self._age
a1=A("sruthi",20,"female")
a2=A("Manoj",18,"male")
print(a1.display())
a1.setAge(22)
print(a1.display())

#Abstraction:
from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self,balance):
        self.__balance= balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def getBalance(self):
        return self.__balance
    @abstractmethod
    def interestcalc(self):
        pass
class SavingAccount(BankAccount):
    def interestcalc(self):
        return self.__balance*0.05
    
#inheritance:
#polymorphism:
class Animal:
    print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Woof")
class Cat(Animal):
    def sound(self):
        print("Meow")'''