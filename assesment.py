#lists for storing name of goodie and price
li1=[]
li2=[]
f=open("assesment1.txt",'r')#Reading from input file
data = f.read() 
print(type(data)) 
database=data.split('\n')
x=database[0]
y=database[0].split(":")
n=int(y[1])#for getting our number of employees
#Used 4 because we have to skip some lines in input file to reach our data
for i in range(4,len(database)):
    print(database[i])
    y=database[i].split(":")
    li1.append(y[0])
    li2.append(int(y[1]))
print(li1,li2)
item=len(li1)
#Sorting step using price
for i in range(0,item):
    for j in range(i+1,item):
        if li2[i]>li2[j]:
            temp=li2[i]
            li2[i]=li2[j]
            li2[j]=temp
            temp1=li1[i]
            li1[i]=li1[j]
            li1[j]=temp1            
diff=li2[n-1]-li2[0]
li3=[0]*n
li4=[0]*n
li4[0:n]=li2[0:n]
li3[0:n]=li1[0:n]
print(li3,li4)
#Selecting the required number of elements to get the minimum difference
for i in range(1,item+1):
    count=i+n-1
    temp=li2[count]-li2[i]
    print(temp)
    if temp<diff:
        li4[0:n]=li2[i:count+1]
        li3[0:n]=li1[i:count+1]
        diff=temp
    count+=1
    if count >= item:
        break
print(li3,li4)
f.close()
#File operation for writing to output file
f2=open("out.txt",'w')
f2.write("The goodies selected for distribution are:\n")
f2.write("\n")
for i in range(len(li3)):
    f2.write(li3[i]+" : "+str(li4[i])+"\n")
f2.write("\n")
f2.write("And the difference between the chosen goodie with highest price and the lowest price is "+ str(diff))
