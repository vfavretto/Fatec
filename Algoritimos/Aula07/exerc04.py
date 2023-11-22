while True:
    base = float(input("Entre com o valor da base: "))
    if base > 0:
        break
    print('O valor é invalido.')

while True:
    altura = float(input("Entre com o valor da altura: "))
    if altura > 0:
        break
    print('O valor é invalido.')

area = base * altura / 2
print(f'A área do triangulo é {area:.2f}')
