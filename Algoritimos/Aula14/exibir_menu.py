
def exibir_menu():

    while True:
        print("Menu de Opções:")
        print("1 - Cadastrar")
        print("2 - Exibir Frase")
        print("3 - Sair")

        opcao = input("Escolha uma opção (1-3): ")

        if opcao.isdigit() and 1 <= int(opcao) <= 3:
            return int(opcao)
        else:
            print("Opção inválida. Por favor, escolha um número entre 1 e 3.\n")

