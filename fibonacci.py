                  
a=int(input("Enter the terms : "))
n1=0
n2=1
if a<=0:
    print("The series is",n1)
else:
    print(n1,n2,end=" ")
    for x in range(2,a):
        n3=n1+n2                           
        print(n3,end=" ")
        n1=n2
        n2=n3
