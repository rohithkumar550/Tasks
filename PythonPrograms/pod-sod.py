n = int(input())
l1 = []
prd = 1

while n > 0:
    l1.append(n % 10)
    n = n // 10

for i in l1:
    prd *= i

res = prd - sum(l1)
print(res)
