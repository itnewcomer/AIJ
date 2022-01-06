A_l = list(map(int,input().split()))
all_num = len(A_l)
num_1_count = A_l.count(1)
if num_1_count > all_num - num_1_count:
    print('1')
else:
    print('2')


