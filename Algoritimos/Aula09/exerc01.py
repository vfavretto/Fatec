lista = []

for i in range(0, 10):
    lista.append(int(input(f'Digite o número {i+1}: ')))

lista.reverse()
print(lista)
