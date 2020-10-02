n=int(input('enter a number'))
a=0
b=1
print(a,b,end=" ")
for i in range(3,n+1):
    s=a+b
    print(s,end=" ")
    a=b
    b=s
