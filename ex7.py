lista = [0,1,2,0,4,10,0,70,-20,0,11,12,14,0,22]

valorremovido = 0
listafinal = filter(lambda val: val != valorremovido, lista)
print(list(listafinal))