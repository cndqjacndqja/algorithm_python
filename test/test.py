n, k=map(int,input().split())
arr=[i for i in range(1, n+1)]

ans=list()
idx=0

for i in range(n):
  idx=(idx+k-1)%len(arr)
  ans.append(arr.pop(idx))

print("<", end='')
for a in ans:
  if a==ans[-1]:
    print(a, end=">")
  else:
    print(a, end=', ')