'''
Venci Ivoš
Zadatak:
- Pronalazak nultocke metodom bisekcije u konacno mnogo koraka

Definirane su tri razlicite funkcije.
-bisekcija - unutar ove funkcije se vrsi postupak bisekcije i broji
    se koliko je koraka potrebno za dobivanje nultocke.
-iteracija - unutar ove funkcije se vrsi racunanje c_n
-funkcija - unutar ove funkcije se nalazi funkcija za koju trazimo nultocku
'''

def bisekcija(a,b):
    '''
    Unutar funkcije bisekcija se trazi unos decimalne tocke 10*n za
    odredjivanje preciznosti nultocke, i vrsi se provjera dali je unos ispravan (mora biti prirodni broj).
    Nakon ispravnog unosa krece metoda bisekcije te se pozivaju pomocne funkcije dok se ne ispune zadani uvjeti.
    Brojac nesmije proci 200 koraka i vrijednost funkcije mora postići trazenu preciznost.
    '''
    n=0
    while n<=0:
        try:
            n=int(input('Unesite decimalnu preciznost:'))

            if n<0:
                print('Unjeli ste negativan broj')

        except:
            print('Niste unjeli valjanu vrijednost!')
    br=0
    c=iteracija(a,b)
    f_x=funkcija(c)
    if (b>0 and a<=0) or a<0:
        while abs(f_x)>1*10**-n and br<200:
            c=iteracija(a,b)
            f_x=funkcija(c)
            if f_x<0:
                a=c
            else:
                b=c
            br+=1
            print('n_%i,\t f_x=%f,\t c_%i=%f,\t a_%i=%f,\t b_%i=%f'%(br,f_x,br,c,br,a,br,b))
    else:
        while abs(f_x)>1*10**-n and br<200:
            c=iteracija(a,b)
            f_x=funkcija(c)
            if f_x<0:
                b=c
            else:
                a=c
            br+=1
            print('n_%i,\t f_x=%f,\t c_%i=%f,\t a_%i=%f,\t b_%i=%f'%(br,f_x,br,c,br,a,br,b))
    print('Nultocka je element [%f,%f] intervala izracunata u %i koraka'%(a,b,br))

def funkcija(x):
    f=x**2+3*x-4
    return f

def iteracija(a,b):
    c=(a+b)/2
    return c

def main():
    '''
    Unutar tijela glavnog programa trazi se unos intervala na kojem cemo raditi
    bisekciju. Te se vrse provjere da su uneseni ispravni podaci.
    Nakon unosa podataka nad vrijednostima a i b pozivamo funkciju funkcija da dobijemo njihove nove vrijednosti
    koje prosljedjujemo u funkciju bisekcija.
    Program nakon izvodjenja bisekci nudi unos novod intervala za novu bisekciju ili unos fraze exit za izlaz.
    '''
    print('Bisekcija funkcije f(x)=x^2+3x-4')
    y=0
    var=''
    while var!='exit':
        while y<2:
            var=input('Unesite vrijednost [a,b] odvojene razmakom ili za izlaz upisite exit:')
            lista=var.split()
            for i in lista:
                try:
                    float(i)
                    y+=1
                except:
                    if var=='exit':
                        y=2
                        break
                    else:
                        print('Niste unjeli valjane vrijednosti')
                        y=0
        if var=='exit':
            print('Hvala i doviđenja:')
            break
        else:
            y=0
            a=funkcija(float(lista[0]))
            b=funkcija(float(lista[1]))
            bisekcija(a,b)
main()
