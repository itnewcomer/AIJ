a = float(input())
pi = 3.141592653589

Area = a * a * pi
Round = 2 * a * pi

print(str("{:.5f}".format(Area)) + ' ' + str("{:.5f}".format(Round)))
