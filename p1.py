#sum of n numbers using recursion

def sum(a,i,l,s):
    if(i==l):
        return s
    else:
        s=s+a[i]
        return sum(a,i+1,l,s)
def main():
    print("Enter a list")
    print("Enter size of list")
    n=int(input())
    list=[]
    for i in range(0,n,1):
        print("Enter {} index".format(i))
        x=int(input())
        list.append(x)
    print(list)

    t=sum(list,0,n,0)
    print("Sum of all numbers of the list is ",t)
if(__name__=="__main__"):
    main()
