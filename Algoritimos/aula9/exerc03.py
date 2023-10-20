from random import randint

dado = [0]*7
estatistica = [0]*7

for i in range(6000):
    x = randint(1,6)
    dado[x] = dado[x] + 1

for i in range(1, 7):
    estatistica[i] = dado[i] / 6000

for i in range(1, 7):
    print(f"O lado {i} foi sorteado {dado[i]} vezes = {estatistica[i]:.2%}")