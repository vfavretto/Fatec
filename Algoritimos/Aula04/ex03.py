Ano_de_Nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = (ano_atual - Ano_de_Nascimento)
Meses = (idade * 12)
dias = (idade * 365)
semanas = (idade * 53)

print('Sua idade: ', idade, "\n" 'Sua idade em meses: ', Meses, "\n")
print('sua idade em dias: ', dias, '\n' 'sua idade em semanas', semanas, '\n')
