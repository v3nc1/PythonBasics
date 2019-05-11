f_in=open('ulaz3.txt','r')
f_out=open('izlaz3.txt','r+')
br=0

for lines in f_in:
    br+=1
    f_out.write(str(br)+'. '+lines)


f_in.close()
f_out.close()
