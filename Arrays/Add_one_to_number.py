n=list(map(int,input().split()))
s=""
l=[]
for i in range(len(n)):
    s=s+str(n[i])
s=int(s)+1
x=str(s)
for i in range(len(x)):
    l.append(int(x[i]))
print(l)    



