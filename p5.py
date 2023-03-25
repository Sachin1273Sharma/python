''' 
reverse the list 

'''
print("Enter elements of the list")
n=int(input())
list=[]
for i in range(0,n,1):
    print("Entrer",i,"index",sep=" ",end="\n")
    x=int(input())
    list.append(x)
print(list)
for i in range(0,int(n/2)+1,1):
 temp=list[i]
 list[i]=list[n-1-i]
 list[n-1-i]=temp
print (list)
