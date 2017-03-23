
resp = 0

for i in range(100,999):
    for j in range(100,999):
        teste = i * j
        strteste = str(teste)
        if strteste == strteste[::-1] and teste > resp:
            resp = teste

print(resp)