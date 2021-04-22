def ReverseAarray(n):
    l=len(n)
    j=l-1
    i=0
    temp=0
    while i<j:
        temp=n[i]
        n[i]=n[j]
        n[j]=temp
        j=j-1
        i=i+1
    print(n)    
n=list(map(int,input().split()))
ReverseAarray(n)

