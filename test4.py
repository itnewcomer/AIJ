N = int(input())
S = input()
S_list = list(S)
if len(set(S_list)) >= 3:
    print('Yes')
else:
    print('No')
