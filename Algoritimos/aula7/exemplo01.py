soma = 0
for i in range(1, 11):
    n = int(input(f'Entre com a {i}° idade'))
    soma = soma + n
media = soma / 10
print(f'A media das idades é {media:5.2f}')
