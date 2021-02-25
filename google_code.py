fyl=open("sample.txt","r")
k=fyl.readline()
arr=k.split()

for i in range(len(arr)):
     x= int(arr[i])
     arr[i]=x
    


streetno=arr[2]
arr1=[]
dict1={}
for i in range(streetno):
      arr1.append(fyl.readline())
      x=arr1[i].split()
      dict1.update({x[2]:[x[0],x[1],x[3]]})

print(dict1)

cars=arr[3]



