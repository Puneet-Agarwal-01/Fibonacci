n = int(input("Enter no. of digit you want to print in fabonacci series:"))
a = 0
b = 1
print("The fibonacci series of",n,"terms is: " , end='')
print(a , end='')
print(' ,',b , end='')

for i in range(3,n+1):
    c = a+b
    print(" ,",c , end='')
    a = b
    b = c

