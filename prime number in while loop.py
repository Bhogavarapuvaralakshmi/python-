n=int(input('enter a number'))
count=0
i=1
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print(n,'is a prime number')
else:
    print(n,'is not a prime number')
