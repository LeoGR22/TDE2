lista = []

while True:
    numeros = int(input("Digite um numero positivo"))
    if numeros >= 0:
        lista.append(numeros)
    else:
        break
#A)
print(lista)
#B)
maior = 0
for x in lista:
   if x < 5:
       maior = maior + 1
print(maior)
#C)
pares = []
for x in lista:
    if x % 2 ==0:
        pares.append(x)
print(sum(pares))
#D)
impares = []
for x in lista:
    if x % 2 != 0:
        impares.append(x)
print(sum(impares))
#E)
print(len(lista))




