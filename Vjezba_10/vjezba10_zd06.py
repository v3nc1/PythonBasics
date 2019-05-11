def sort_lista(l):

    lista=[]

    while len(l)!=0:
        br=0
        d=len(l)
        ind_min=0

        for i in range(1,d,2):
            if br==0:
                ind_min=l[i]
                br_ind=i


            if l[i]<ind_min:
                ind_min=l[i]
                br_ind=i

            br+=1
        lista.append(l[br_ind-1])
        lista.append(l[br_ind])
        l.remove(l[br_ind])
        l.remove(l[br_ind-1])

    return lista




f_in=open('ulaz6.txt','r')
f_out=open('izlaz6.txt','w')

ime=''
wight=0
hight=0
lista=[]
lista_2=[]
sortana=[]
br=1


lista_2+=f_in.read().split()

for i in lista_2:

    if br==1:
        ime=i

    elif br==2:
        wight=float(i)
    elif br==3:
        hight=float(i)
        br+=1
    if br==4:
        lista.append(ime)
        lista.append('%.2f'%(wight/(hight**2)))
        ime=''
        weight=0
        height=0
        br=0
    br+=1
sortana+=sort_lista(lista)



for i in range(1,len(sortana),2):
    f_out.write(sortana[i-1]+' '+sortana[i]+'\n')


f_in.close()
f_out.close()
