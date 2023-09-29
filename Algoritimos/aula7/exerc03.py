k = int(input("Digite um número inteiro maior que 1: "))
primo = True
n = 0
for i in range(1, k+1):
    if (k % i) == 0:
        n = n + 1

if n > 2:
    primo = False

if primo:
    print(f"{k} é um número primo.")
else:
    print(f"{k} não é um número primo.")
