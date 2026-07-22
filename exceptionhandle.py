x = int(input("enter a number:"))
y = int(input("enter a number:"))
print(x/y)


x = int(input("enter a number:"))
y = int(input("enter a number:"))
try:
    print(x/y)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
finally:
    print("done")
    
for i in range(5):
    print(i)
else:
    print("done")
    
for i in range(5):
    if i == 4:
        break
        print(i)
else:
    print("done")
    
try:
    a = int(input("enter a number:"))
    print(a)
except ValueError as e:
    print(e)
else:
    print("done")

#to throw error   
a = int(input("enter a number:"))
if a<0:
    raise ValueError("number is negative")
else:
    print(a)
    
#task 1
## keep asking valid integer number
## if not valid integer number,print error
while True:
    try:
        a = int(input("enter a number:"))
        print(a)
        break
    except ValueError as e:
        print(e)

#task2
## handle index error while accessing list element if it is out of range handle it
l = [1,2,3,4,5,6,7,8,9,10]
try:
    print(l[10])
except IndexError as e:
    print(e)
