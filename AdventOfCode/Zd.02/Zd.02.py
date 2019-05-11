fIn=open("input.txt","r")

file=[]

for line in fIn:
    file.append(line.rstrip())

fIn.close()



count_2=0
count_3=0


for i in range(len(file)):
    count=0
    temp=[]
    var=file[i]
    br_2=0
    br_3=0

    for n in range(len(var)):
        count=0

        if var[n] not in temp:

            temp.append(var[n])
            count=var.count(var[n])
        if count==2 and br_2<1:
            count_2+=1
            br_2+=1
        elif count==3 and br_3<1:
            count_3+=1
            br_3+=1

print("Count 2= ",count_2)
print("Count 3= ",count_3)
print("Result= ",count_2*count_3)

v="tata"
v2="teta"


temp=[]
for i in range(len(file)):
    count=0
    var=file[i]

    br_3=0

    for n in range(i+1,len(file)):
        br_2=0
        var_2=file[n]
        ##if len(var)==len(var_2):
        for l in range (len(var)):
            if var[l]!=var_2[l]:

                br_2+=1

        if br_2==1:
            temp.append(var)
            temp.append(var_2)
var=temp[0]
var_2=temp[1]
id=""
for l in range(len(temp[0])):
    if var[l]==var_2[l]:
        id+=var[l]

print(temp)
print(id)
