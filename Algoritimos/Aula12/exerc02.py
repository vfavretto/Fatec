lista1 = []
lista2 = []
for i in range(1, 6):
    a = input(f"insira o {i}º número da lista 1: ")
    lista1.append(a)

for i in range(1, 6):
    b = input(f"insira o {i}º número da lista 2: ")
    lista2.append(b)

c = set(lista1)
d = set(lista2)

print(f"Lista 1: {c} \nLista 2: {d}")
print(f"União das listas: {c.union(d)}")