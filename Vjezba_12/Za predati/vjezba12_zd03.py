f_in=open('ulaz.txt','r')
f_out=open('izlaz.txt','w')
lista=[]
lista_sort=[]
br=0

for i in f_in.readlines():
    lista.append(i.split())

lista_sort=sorted(lista,key=lambda ime:ime[1])

for i in range(len(lista_sort)):
    br+=1
    f_out.write('%i. %s %s\n'%(br,lista_sort[i][0],lista_sort[i][1]))


f_in.close()
f_out.close()
