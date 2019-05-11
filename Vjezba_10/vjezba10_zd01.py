f_in=open('ulaz1.txt','r')


for i in f_in.read():
    if i.isalpha():

        print(i,end='')


f_in.close()
