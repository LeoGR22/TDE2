import random
lista = []
lista = [random.randint(0, 20) for x in range(0,51)]

#A)
soma = sum(lista)
print(soma)
#B)
repetido = lista.count(lista[9])
print(repetido)
#C)
print(max(lista))
#D
print(min(lista))
