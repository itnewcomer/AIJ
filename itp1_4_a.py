a,b = map(int, input().split())
a1 = a // b
a3 = a / b
a2 = a % b

print(str(a1) + ' ' + str(a2) + ' ' + str("{:.5f}".format(a3)))
