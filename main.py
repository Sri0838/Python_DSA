print("sruthi\nsruthi sri")
print("\\tcurrent\\new\\folder")
# \ is escape character
print(r"\tcurrent\new\folder")

#write a program to find odd and even with function:
def check(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
check(10)

#print the append and pop of list
l = [1,2,3,4]
l.append(5)
l.pop(2)
print(l)

#dictionary
dict = {
    "name" : "Sruthi",
    "gender" : "Female",
    "age" : 20,
    "courses" : ["python","java","datascience"]
    }
dict["name"] = "sruthi sri"
dict.update({"courses": ["python", "java", "machine learning"]})
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())

def count(*args):
    print(type(args))
#count(1,2,3,4,5)
def dict(**kwargs):
    print(type(kwargs))
#dict(name="sruthi",age = 20,gender = "female")
def default(gender,name = "sruthi",age = 20):
    print(name,age,gender)
    
#OOPS
l = [1,2,3]
s="String"
print(len(l))
print(len(s))
 #4 pillars of OOPS
 #Encapsulation:
 #Abstraction:
 #Inheritance:
 #polymorphism:
x = 10
x = "data"
 
# take a string as input and
# print it back by removing the first and last character of the input string
x = "Sruthi"
x = x[1:-1]
print(x[::-1])

#create an example while loop which will not terminate, and prints hi in each iteration
#and how will you stop the program manually?
while True:
    print("hi")
    
#take a number as input and find the sum of numbers from 1 to that number
n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)
  
