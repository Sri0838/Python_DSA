'''15#row by row pattern
n = 5
for i in range(n):
    print("*")

#In 1 row pattern 
n = 5
for i in range(n):
    print("*",end = " ")

#square pattern
n = 5
for i in range(n):
    for j in range(n):
        print("*",end = " ")
    print()

#right angled triangle pattern    
n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end = " ")
    print()

#inverted right angled triangle pattern   
n = 5
for i in range(n,0,-1):
    for j in range(i):
        print("*", end = " ")
    print()
    
#Diamond pattern
#first how many rows
#how many spaces
#how many stars
n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end = " ")
    for j in range(2*i+1):
        print("*", end = " ")
    print()
for i in range(n-2,-1,-1):
    for j in range(n-i-1):
        print(" ",end = " ")
    for j in range(2*i+1):
        print("*", end = " ")
    print()
    
#Armstrong Number
n = int(input("enter a number:")) #153
sum = 0
temp = n                 #153 
while temp > 0:          #153 15  1
    digit = temp%10      #3   5   1  
    sum += digit**3      #27  125 153
    temp //= 10          #15   1  0
if sum == n:             # 153 == 153  
    print(n, "is an Armstrong Number")
    
# Hollow square pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*",end = " ") 
        else:
            print(" ",end = " ")
    print() 

#pascals pattern'''

