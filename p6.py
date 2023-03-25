#sort the list using insertion sort
list=[]
print("Enter no of elements to be inserted in list ")
n=int(input())
for i in range(0,n,1):
    print("Enter {} index".format(i))
    x=int(input())
    list.append(x)
print(list)
print("list after sorting is :")
for i in range(1,n,1):
    key=list[i]
    j=i-1
    while(j>=0 and list[j]>key):
        list[j+1]=list[j]
        j=j-1
    list[j+1]=key
print(list)