#Venci Ivos
#Kolokvij II zadatak 1

from random import*

n=int(input('Unesi cijeli broj:'))
lista=[]
naj_suma=0
index_suma=0
if n<=0:
    print('Niste unjeli broj u trazenom rasponu!')

else:
    for i in range(5):
        lista.append([])
        for j in range(n):
            lista[i].append(randint(0,10))
        if naj_suma<sum(lista[i]):

            naj_suma=sum(lista[i])
            index_suma=i

print('Generirane liste su: %s \n Lista s najvecom sumom je %s'%(lista,lista[index_suma]))
