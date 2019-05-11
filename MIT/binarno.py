n=0

while n!='x':
    n=input('Unesi broj za pretborbu u binarni:')
    b=''
    v=0
    if n!='x':
        temp=int(n)

        while temp!=0:
            b+=str(temp%2)
            temp//=2

        print('Binarni oblik broja %s je %s'%(n,b[::-1]))

    for i in range(len(b)):
        v+=int(b[i])*2**i
    print('Pretvorba natrag u decimalni oblik %i'%(v))
