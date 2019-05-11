from random import*

def loto_izvlacenje():
    loto=[]

    for i in range(7):
        loto.append(randint(1,39))
    return loto

def provjera(l_1,l_loto):

    br=0

    for i in l_1:
        if i in l_loto:
            br+=1
    return br

br=1
lista=[]
loto=[]
pogodak=0
while br<8:
    try:
        n=int(input('Odaberite %i broj za loto 7/39:'%(br)))

        if n<1 and n>39:
            print('Odabrali ste pogrešan broj!')
        elif n in lista:
            print('Broj je vec odabran!')
        else:
            lista.append(n)
            br+=1
    except:
        print('NISTE UNJELI BROJ')


loto=loto_izvlacenje()
pogodak=provjera(lista,loto)
print('Izvuceni su brojevi %s'%(*loto))
if pogodak==7:
    print('JACKPOT')
else:
    print('Pogodili ste %i brojeva! Čestitam :)'%(pogodak))
