salario = float(input('Digite seu salario: '))
aumento = salario * 1.25
# Dentro da função dentro de ".2f" eu posso determinar o número total ex: '8.2f'
# Desta forma ele ficaria com um total possivel de caracteres contando com o ponto
print(f'Salario depois do aumento de 25%: R$ {aumento:.2f}')
