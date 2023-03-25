#pascal triangle
print("Enter n")
n=int(input())
t=n

for i in range(0,n,1):
    
    for j in range(1,t,1):
        print(" ",end="")
    for k in range(0,i+1,1):
        if(i==0 or k==0):
            p=1
        else:
            p=int(p*((i-k+1)/k))
        print(p," ",end="")
    t=t-1
    print()

        