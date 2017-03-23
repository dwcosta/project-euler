
import math

def primo(n):
    if n < 0:
        return False
    for j in range(2, int(math.sqrt(n)+1)):
        if n % j == 0:
            return False
    return True

numerodado = 600851475143

multi = 1

while multi * multi <= numerodado:
    multi += 2
    if numerodado % multi == 0:
        if primo(multi):
            maximo = multi

print(maximo)