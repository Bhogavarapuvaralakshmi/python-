mid='aaa@111'
pwd='9876'
for i in range(10):
    umid=input('enter a mail id')
    upwd=input('enter a password')
    if umid==mid and upwd==pwd:
        print('login succesfully')
        break
    else:
        print('wrong credentials')
else:
    print('account blocked')
