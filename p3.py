#reverse a string in python using recursion
print("Enter a string")
s=input()
print("String is",s)
def reverse(s,r,x):
    if(r==-1):
        return x
    else:
        x=x+s[r]
        return reverse(s,r-1,x)
print("Reverse of string is :",reverse(s,len(s)-1,""))

    