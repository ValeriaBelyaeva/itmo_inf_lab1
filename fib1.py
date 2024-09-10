fl = open("input")
n = int(fl.readline())
fl.close()

fl = open("output", 'w')
fib = [0 for i in range(n+1)]
fib[1] = 1
for i in range(2, n+1):
    fib[i] = fib[i-1]+fib[i-2]

fl.write(str(fib[n]))
fl.close()