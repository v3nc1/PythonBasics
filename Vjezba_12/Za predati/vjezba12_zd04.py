#Venci Ivos
#Vjezba 12 zadatak 4

def povrsina_trokuta(t_1,t_2,t_3):

    p=(1/2)*abs(int(t_1[0])*(int(t_2[1])-int(t_3[1]))+int(t_2[0])*(int(t_3[1])-int(t_1[1]))+int(t_3[0])*(int(t_1[1])-int(t_2[1])))

    return p

t_1=(input('Unesi T 1 koordinatu:').split())
t_2=(input('Unesi T 1 koordinatu:').split())
t_3=(input('Unesi T 1 koordinatu:').split())

povrsina=povrsina_trokuta(t_1,t_2,t_3)


if povrsina==0:

    print('Točke ne tvore trokut')
else:
    print('Površina trokuta je %.2f'%(povrsina))
