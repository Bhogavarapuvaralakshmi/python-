n=int(input('enter a number'))
a=0
b=1
for i in range(3,n+1):
    s=a+b
    a=b
    b=s
    if b>=n:
        print(a)
        break
