N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = []
while N > 0 or M > 0:
    if N == 0:
        t = B
        M = M-1
    if M == 0:
        t = A
        N = N-1
    if A[0] > B[0]:
        t = B
        M = M-1
    else:
        t = A
        N = N-1
    C
