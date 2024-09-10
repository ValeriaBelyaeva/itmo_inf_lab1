fl = open("input")
n = int(fl.readline())
fl.close()

fl = open("output", 'w')
a, b = 0, 1
for i in range(2, n+1):
    a, b = b, (a+b)%100

fl.write(str(b%10))
fl.close()