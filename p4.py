'''
1/0 pattern
1
10
101
1010
10101

'''
print("Enter n")
n=int(input())
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        if(j%2==0):
            print("0",end="")
        else:
            print("1",end="")
    print()