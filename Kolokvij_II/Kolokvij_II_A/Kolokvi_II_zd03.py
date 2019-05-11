f_in=open('ulaz.txt','r')

lista=list(f_in.read().split())
mali=0
br_index=0

for i in range(1,len(lista),2):
    if mali==0:
        mali=int(lista[i])

    elif mali>int(lista[i]):
        br_index=i
        mali=int(lista[i])

print('Najmanji grad je %s sa brojem stanovnika od %s'%(lista[br_index-1],lista[br_index]))
