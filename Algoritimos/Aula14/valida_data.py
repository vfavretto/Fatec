from datetime import datetime
def valida_data(data_str):
    try:
        data_nasc = datetime.strptime(data_str, "%d/%m/%Y").date()

        hoje = datetime.now().date()

        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

        if idade >= 18:
            return True, "Cadastro válido."
        else:
            return False, "Cadastro inválido. Menor de 18 anos."
    except ValueError:
        return False, "Data inválida."

#data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

#resultado, mensagem = valida_data(data_nascimento)

#print(mensagem)
