n = int(input())
list_a = list(map(int,input().split()))

for i in range(n):
    i += 1
    if i == n:
        print(str(list_a[-i]))
    else:
        print(str(list_a[-i]) + ' ',end ='')

