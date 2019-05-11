
def broji_znamenke(znamenka,niz):
    br=0
    d=len(niz)

    for i in range(d):

        if znamenka==niz[i]:

            br+=1

    return(br)



f_in=open('ulaz5.txt','r')
f_out=open('izlaz5.txt','w')

niz=f_in.read()
niz_2=''
br=0

for i in niz:

    if i.isdigit():


        if not i in niz_2:
            niz_2+=i
    else:
        niz=niz.replace(i,'')
d=len(niz)
lista=list(niz_2)
lista.sort()
print(lista,niz)

for j in lista:
    br=broji_znamenke(j,niz)
    f_out.write(j+'-'+str(br/d)+'\n')




f_in.close()
f_out.close()
