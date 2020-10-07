a=int(input('enter a number'))
for j in range(a-1,1,-1):
    for i in range(2,j):
        if j%i==0:
            break
        else:
            bp=j
            print(j)
            break
j=a
while True:
    for i in range(2,j):
        if j%i==0:
            break
    else:
        ap=j
        print(j)
        break
    j+=1

if abs(a-ap)>abs(a-bp):
    print(bp,'nearest prime')
elif abs(a-ap)<abs(a-bp):
    print(ap,'nearest prime')
else:
    print(ap,bp,'nearest prime')
