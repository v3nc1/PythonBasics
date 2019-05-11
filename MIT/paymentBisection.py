
#ulazni podaci
balance=320000
annualInterestRate=0.2



#dio koda
months=12
a=balance/12
b=((balance/a)/100)
bal=balance
c=1
br=0


while bal>=0:

    bal=balance

    b+=0.001
    c=(balance*b)

    for i in range(months):

        bal-=(balance*b)
        bal+=bal*annualInterestRate
        print(i+1,bal)
        '''    if bal<0:
        b=c
    else:
        a=c
        '''
    br+=1
    print(br,round(bal,2))

    if br==100:
        break






#izlaz

print('Lowest Payment:',c,a,b)
