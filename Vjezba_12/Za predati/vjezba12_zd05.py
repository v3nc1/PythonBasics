#Venci Ivos
#Vjezba 12 zadatak 5


from turtle import*
from random import*

m=300
b=0
br=0

while br==0:
    try:

        n=int(textinput('Faktor umanjenja','Unesi broj veci od 0 a manji od 50'))

        if n>0 and n<50:

            colormode(255)

            for j in range(5):

                b=randrange(0,256)
                begin_fill()
                fillcolor(b,b,b)
                for i in range(3):

                    fd(m)
                    lt(360/3)
                m-=n
                end_fill()
            br+=1
            exitonclick()
        else:
            print('NISTE UNJELI BROJ U TRAZENOM RASPONU!!!')
    except:
        print('NISTE UNJELI BROJ!!!')
