from valida_cpf import valida_cpf
from valida_data import valida_data
from exibir_menu import exibir_menu
import random

while True:
    opcao = exibir_menu()

    if opcao == 1:
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")

        cpf = input("Digite o CPF (formato: 999.999.999-99): ")
        while not valida_cpf(cpf):
            print("CPF inválido. Tente novamente.")
            cpf = input("Digite o CPF (formato: 999.999.999-99): ")

        data_nascimento = input("Digite a data de nascimento (formato: dd/mm/aaaa): ")
        while not valida_data(data_nascimento):
            print("Data de nascimento inválida. Tente novamente.")
            data_nascimento = input("Digite a data de nascimento (formato: dd/mm/aaaa): ")

        renda_bruta = float(input("Digite a renda bruta: "))

    elif opcao == 2:
        mensagens_motivacionais = [
            "A persistência realiza o impossível",
            "Seus sonhos não precisam de plateia, eles só precisam de você",
            "A persistência é o caminho do êxito",
            "No meio da dificuldade encontra-se a oportunidade"
        ]

        mensagem_aleatoria = random.choice(mensagens_motivacionais)
        print("Mensagem Motivacional:")
        print(mensagem_aleatoria)

    elif opcao == 3:
        print(f"Tchauzinho, até mais! :)")
        break
