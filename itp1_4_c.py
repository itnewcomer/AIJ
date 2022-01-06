while True:
    a,b,c = map(str, input().split()) 
    a = int(a)
    c = int(c)
    if b == '+':
        print(str(a+c))
    if b == '-':
        print(str(a-c))
    if b == '*':
        print(str(a*c))
    if b == '/':
        print(str(a//c))
    if b == '?':
        break

