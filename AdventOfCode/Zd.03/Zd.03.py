fIn=open("input.txt","r")

file=[]
num=[]

for line in fIn:
    file.append(line.rstrip())

fIn.close()

val=[]
position=[]
size=[]


for i in file:
    val+=i.split("@")

for i in range(1,len(val),2):
    num+=val[i].split(":")

for i in range(0,len(num),2):
    position+=num[i].split(",")
for i in range(1,len(num),2):
    size+=num[i].split("x")
'''
print(position)
print(size)
'''


br=1
n = 1000
size_x=0
size_y=0
position_x=0
position_y=0
fabric = [[0] * n for i in range(n)]
ord_num=1
wanted=[]
orders=[]
print("First")
for i in range(len(size)):

    if br==1:
        size_x=int(size[i])
        position_x=int(position[i])
        br+=1
    else:
        size_y=int(size[i])
        position_y=int(position[i])
        br=1
        orders.append(ord_num)
        for y in range(size_y):
            for x in range(size_x):
                if fabric[position_y+y][x+position_x]==0:
                    fabric[position_y+y][x+position_x]=ord_num
                else:

                    fabric[position_y+y][x+position_x]="."
        ord_num+=1
'''
for a in fabric:

    print(a)
'''
br=1
ord_num=1
size_x=0
size_y=0
position_x=0
position_y=0
wanted_add=[]
wanted_rem=[]
flag=False
print("second")
for i in range(len(size)):

    if br==1:
        size_x=int(size[i])
        position_x=int(position[i])
        br+=1
    else:
        size_y=int(size[i])
        position_y=int(position[i])
        br=1

        flag=False
        for y in range(size_y):
            for x in range(size_x):
                if fabric[position_y+y][x+position_x]==ord_num:
                    flag=True

                else:
                    flag=False
                    continue


        ord_num+=1
        print(ord_num," ",flag)
        if flag:
            wanted_add.append(ord_num-1)



width=0
width_x=[]
flag=False
area=0
print("third")
for row in fabric:


    if flag:

        flag=False
        width_x.append(width)
    width=0
    for cell in row:

        if cell==".":
            width+=1
            flag=True


for n in width_x:
    area+=n

print("Square inch = ",area)

print(len(wanted_add))
