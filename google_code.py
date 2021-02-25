fyl=open("sample.txt","r")
k=fyl.readline()
arr=k.split()

for i in range(len(arr)):
     x= int(arr[i])
     arr[i]=x
    


streetno=arr[2]
arr1=[]
streets={}
for i in range(streetno):
      arr1.append(fyl.readline())
      x=arr1[i].split()
      streets.update({x[2]:[x[0],x[1],x[3]]})



carsno=arr[3]
arr2=[]
cars={}
l=0
for i in range(carsno):
    arr2.append(fyl.readline())
    x=arr2[i].split()
    cars.update({"cars"+str(l):x})
    l=l+1

print(cars)

        



