from turtle import*

niz='ABCD'
pu()
goto(-200,-200)
pd()



for i in range(4):

    fd(400)
    lt(90)
for i in niz:
    pu()
    bk(20)
    fd(20)
    write(i,font=10)
    fd(400)
    lt(90)
    pd()
