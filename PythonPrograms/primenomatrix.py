def isprime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n=int(input())
matrix=int(input())
l1=list(range(1,n))
l2=list(map(isprime,l1))
res=[]
for i in range(len(l1)):
    if l2[i]==True:
        res.append(l1[i])

for i in range(0,len(res),matrix):
    print(res[i],res[i+1])
