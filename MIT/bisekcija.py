n=''
lo=0
hi=100
temp=(hi+lo)//2
while n!='c':
    n=input('Jeli veci ili manji od %i:'%(temp))
    if n=='l':
        hi=temp
        temp=(hi+lo)//2
    elif n=='b':
        lo=temp
        temp=(hi+lo)//2
    else:
        print('Bravo')
