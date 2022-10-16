lista = []
for numero in range(1,11):
    lista.append(input("Digite 10 valores"))

repetidos = []

for i in range(len(lista)):
    for j in range(len(lista)):
        if i != j:
            if lista[i] == lista[j] and lista[i] not in repetidos:
                repetidos.append(lista[i])
print("Os numeros repetidos são:" + str(repetidos))
