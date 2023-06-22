import random
palpite = int(input("Qual é o seu númeo do palpite entre 1 e 50:  "))
numero_sorteado = random.randint(1,50)

if palpite > numero_sorteado:
    print("Muito Alto")
elif palpite < numero_sorteado:
    print("Muito Baixo")
else:
    print("Você Acertou")