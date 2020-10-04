n=int(input('enter a number'))
a=n
s=0
while n>0:
    rem=n%10
    s+=rem*rem*rem
    n=n//10
if a==s:
    print(a,'armstrong number')
else:
    print(a,'not armstrong number')
