f_in=open('ulaz7.txt','r')
f_out=open('izlaz7.txt','w')

znak='0'
niz=''
br=0
br_j=0
lista=f_in.read().split()

print(lista)
for i in lista:

    if i.isdigit():
        lista[br]=int(i)

    else:
        niz=''
        znak='0'
        br_j=0
        for j in i:

            if j.isdigit() and znak.isdigit():
                niz+=j
                br_j+=1
            elif br_j>=0 and j.isdigit():
                niz+=j
            elif br_j>0 and not j.isdigit() and int(niz)==0:
                j.replace(j,'0')

            else:
                znak+=j



        lista[br]=int(niz)

    br+=1
lista.sort()

for i in lista:
    f_out.write(str(i)+',')

print(lista)

f_in.close()
f_out.close()
