fyl=open("sample.txt","r")
k=fyl.readline()
arr=k.split()

for i in range(len(arr)):
     x= int(arr[i])
     arr[i]=x
    


streetno=arr[2]
arr1=[]
for i in range(streetno):
      arr1.append(fyl.readline())



