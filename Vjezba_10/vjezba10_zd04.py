f_in=open('ulaz4.txt','r')
f_out=open('izlaz4.txt','w')


for line in f_in:
    br_1=0
    br_2=0
    br_temp=''
    no=0
    izlaz=0

    
    for i in line:
        if i.isdigit() and no==0:
            br_temp+=i
        elif i=='+' or i=='-' or i=='*' or i=='/':

            br_1=int(br_temp)
            operacija=i
            no=1
            br_temp=''
        if no==1 and i.isdigit():
            br_temp+=i


    br_2=int(br_temp)
    if operacija=='+':
        izlaz=br_1+br_2
        f_out.write(str(izlaz)+'\n')
    elif operacija=='-':
        izlaz=br_1-br_2
        f_out.write(str(izlaz)+'\n')
    elif operacija=='*':
        izlaz=br_1*br_2
        f_out.write(str(izlaz)+'\n')
    elif operacija=='/':
        izlaz=br_1/br_2
        f_out.write(str(izlaz)+'\n')

f_in.close()
f_out.close()

f_in=open('ulaz4.txt','r')
f_out=open('izlaz4.txt','r')

print(f_in.read())

print(f_out.read())
