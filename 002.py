soma, fibatual, fibprox = 0, 1, 2

while fibatual <= 4000000:
    if fibatual % 2 == 0:
        soma += fibatual
    fibatual, fibprox = fibprox, fibatual + fibprox

print(soma)
