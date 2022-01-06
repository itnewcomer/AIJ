while True:
    a,b = map(int,input().split())
    if a == 0:
        break
    for i in range(a):
        if i == 0 or i == a-1:
            print("#"*b)
        else:
            for j in range(b):
                if j == 0 or j == b-1:
                    print('#',end='')
                else:
                    print('.', end ='')
            print()
    print()
