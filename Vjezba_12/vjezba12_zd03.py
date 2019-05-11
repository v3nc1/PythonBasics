f_in=open('ulaz.txt','r')
f_out=open('izlaz.txt','w')
lista=[]
lista_sort=[]
lista_index=[]
br=0

for lines in f_in.readlines():
    lista+=(lines)
print(lista,len(lista))

print(sorted(lista,key=lambda n:n[2]))
print(lista_sort)



#print(lista)


f_in.close()
f_out.close()
