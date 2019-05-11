#Venci Ivos
#Vjezba 12 zadatak 2


def samoglasnici(n):

    br=0
    s='aeiou'
    n=n.lower()

    for i in n:
        if i in s:
            br+=1
    return br

s=input('Unesi niz znakova:')
postotak=0
s_glas=0

s_glas=samoglasnici(s)
postotak=(s_glas/len(s))*100


print('U nizu {} ima {} samoglasnika i to je {:.2f}%'.format(s,s_glas,postotak))
