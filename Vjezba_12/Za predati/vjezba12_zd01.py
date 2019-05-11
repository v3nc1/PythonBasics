#Venci Ivos
#Vjezba 12 zadatak 1

from random import*

n=1
br=0
x=0
lista=[]
br_par=0
br_nepar=0

while br!=n:
    try:

        n*=int(input('Unesi cijeli broj veći od 0 do 100:'))

        if n>0 and n<101:
            while n!=br:
                x=randrange(1,101)
                if x not in lista:
                    br+=1
                    if not x%2:
                        br_par+=1
                    else:
                        br_nepar+=1

                    lista.append(x)
            print('U listi %s se nalaze \n %i parnih i %i neparnih brojeva'%(lista,br_par,br_nepar))
        else:
            print('Unjeli ste broj manji od 0!')


    except:
        print('Niste unjeli broj!')
