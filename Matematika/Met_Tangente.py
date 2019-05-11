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


def funkcija(x):
    f=x**2+3*x-4
    return f
def der_f(x):
    f=2*x+3
    return f
def met_tangente(x):

    return x-(funkcija(x)/met_tangente(x))





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
            met_tangente(n)
main()
