def enter_int(texto):
    while 1:
        try:
            x=int(input(texto))
            return x
            break
        except:
            print('Entrada inválida - Tente novamente.')

def primo(x):
    contadiv = 1
    for i in range(1,x):
        div = x % i
        if div == 0:
            contadiv+=1
    if contadiv == 2:
        return True
    else:
        return False
 
num = 2
contador = 1
qty = enter_int("Quantos numeros primos quer listar? ==> ")
while contador <= qty:
    if primo(num) == True:
        contador=contador+1
        print(num) 
    if num % 2 == 0:
        num+=1
    else:
        num+=2
