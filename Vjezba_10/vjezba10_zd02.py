f_in=open('ulaz2.txt','r')

lin=f_in.read()
el=''
br=0

for i in lin:

    br=0
    for j in lin:

        if i==j:
            br+=1

    if br>1:
        if i not in el:
            el+=i

if len(el)==0:
    print('Nijedan znak se ne pojavljuje više od jedan put.')
else:
    print('Znakovi koji se pojavljuju više puta:"%s"'%(el))



f_in.close()
