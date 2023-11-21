def verificarpositivo(num):
    if num > 0:
        return 'P'
    else:
        return 'N'

print(verificarpositivo(int(input('Digite um numero: '))))
