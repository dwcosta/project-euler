x1 = 0
x2 = 1
fib = 0
count = 0
ex = True
dig = 0
ind = 1
while ex == True:
    fib = x1+x2
    x1 = x2
    x2 = fib
    count += 1
    ind += 1
    if (len(str(fib)) == 1000):
        ex = False

print(ind)