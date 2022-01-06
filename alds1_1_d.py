N = int(input())
A =[]
for _ in range(N):
    A.append(int(input()))

maxv = A[1] - A[0]
minv = A[0]

for i in range(1,N):
  maxv = max(maxv, A[i]-minv)
  minv = min(minv, A[i])

print(maxv)
