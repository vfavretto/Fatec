s_peso = 0
s_alturas = 0
maior_imc = 0
menor_imc = 0

for i in range(1, 6):
    peso = float(input(f"Digite o peso da pessoa {i}: "))
    altura = float(input(f"Digite a altura da pessoa {i}: "))
    s_peso = s_peso + peso
    s_alturas = s_alturas + altura
    imc = peso / (altura ** 2)
    if i == 1:
        maior_imc = imc
        menor_imc = imc
    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc

media_peso = s_peso / 5
media_altura = s_alturas / 5

print(f"\nO peso médio é {media_peso:.2f} kg.")
print(f"A altura média é {media_altura:.2f} m.")
print(f"O maior IMC é {maior_imc:.2f}.")
print(f"O menor IMC é {menor_imc:.2f}.")
