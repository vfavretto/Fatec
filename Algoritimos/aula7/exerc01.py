import math
e = 0
n = int(input("Digite um número inteiro positivo: "))
for i in range(1, n+1):
    e = e + math.pow(2, i)
    # ou e = e + (2**i)
print(f"O valor de E é igual a: {e:.2f}")
