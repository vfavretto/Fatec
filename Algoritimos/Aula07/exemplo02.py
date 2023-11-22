soma = 0
qts = int(input('Digite o qts da idade: '))
for i in range(1, qts + 1):
    n = int(input(f'entre com a {i}° idade: '))
    soma = soma + n
media = soma / qts
print(f'A média das idades é igual {media:5.2f}')
