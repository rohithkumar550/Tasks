n=int(input("enter seq numbers"))
l=list(range(1,n+1))
res=[]
matrixsize=int(input("enter matrix dimension"))

for i in range(matrixsize):
    for j in range(i,len(l),matrixsize):
        res.append(l[j])

for i in range(0,len(l),matrixsize):
    for j in range(matrixsize):
        print(res[i+j],end=' ')
    print()
