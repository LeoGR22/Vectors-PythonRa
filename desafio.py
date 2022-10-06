sorteados = [2,16,24,38,43,59]
numeros = []
acertos = 0

for num in range(0,6):
    numeros.append(int(input("Digite os numeros")))
for a in sorteados:
    for j in numeros:
        if (a==j):

            acertos = acertos + 1

print(sorteados)
print(numeros)
print(acertos)






