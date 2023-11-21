def somaimposto(taxaImposto, custo):
    custo += custo * (taxaImposto / 100)
    return f"{custo:.2f}"

valorFinal = somaimposto((int(input('Digite a taxa do imposto em %: '))),
                  (int(input('Digite o custo do produto: '))))

print(valorFinal)