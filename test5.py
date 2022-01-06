N = int(input())
S = input()
counter_A = 0
counter_B = 0
counter_C = 0
counter_D = 0
counter_E = 0
for i in range(N):
    if S[i] == 'A' and counter_A == 0:
        counter_A += 1
    if S[i] == 'B' and counter_B == 0:
        counter_B += 1
    if S[i] == 'C' and counter_C == 0:
        counter_C += 1
    if S[i] == 'D' and counter_D == 0:
        counter_D += 1
    if S[i] == 'E' and counter_E == 0:
        counter_E += 1
    if counter_A + counter_B + counter_C + counter_D + counter_E >=3:
        print('Yes')
        break;
    if counter_A + counter_B + counter_C + counter_D + counter_E < 3 and i == N-1:
        print('No')
