salario = float(input('Digite seu salario: '))
aumento = float(input('Digite o percentual de aumento: '))
percentual = (salario + (salario * aumento) / 100)
print(f'Novo salario: R$ {percentual:.2f}')
