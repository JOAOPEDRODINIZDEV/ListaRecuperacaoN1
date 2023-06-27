import random
palpite = int(input("Qual é o seu númeo do palpite entre 1 e 50:  "))
numero_sorteado = random.randint(1,50)

while palpite != numero_sorteado:
    if palpite > numero_sorteado:
        print("Muito Alto")
        palpite = int(input("Qual é o seu númeo do palpite entre 1 e 50:  "))        
    elif palpite < numero_sorteado:
        print("Muito Baixo")
        palpite = int(input("Qual é o seu númeo do palpite entre 1 e 50:  "))
        
print("Você Acertou")