#Venci Ivos
#Kolokvij II zadatak 2

def interpunkcija(niz):
    br_tocka=0
    br_zarez=0
    br_dvotocka=0
    br_tockazarez=0
    n='.,:;'

    for i in niz:
        if i in n:
            if i=='.':
                br_tocka+=1
            elif i==',':
                br_zarez+=1
            elif i==':':
                br_dvotocka+=1
            else:
                br_tockazarez+=1
    return '%i tocaka, %i zareza, %i dvotocki i %i tocke zareza'%(br_tocka,br_zarez,br_dvotocka,br_tockazarez)


def main():

    niz=input('Unesi niz:')

    print('U stringu ima %s'%(interpunkcija(niz)))

main()
