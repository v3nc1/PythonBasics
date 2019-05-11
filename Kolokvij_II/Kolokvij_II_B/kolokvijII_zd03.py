

f_in=open('ulaz.txt','r')
lista=[]
naj_dat=0
naj_index=0
lista=f_in.read().split()

for i in range(1,len(lista),2):

    
    if int(lista[i])>naj_dat:
        naj_dat=int(lista[i])
        naj_index=i



print('Najveca datoteka je %s velicine %s kB'%(lista[naj_index-1],lista[naj_index]))
f_in.close()
