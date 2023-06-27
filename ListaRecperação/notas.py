def calcular_media(notas,soma):
    media = soma / len(notas)
    
    return media

notas = []
soma = 0

for i in range(10):
    n = float(input(f"Digite a nota do {i+1}° aluno : "))
    notas.append(n)
    soma += n
    
media = calcular_media(notas,soma)



print("\nA média dos alunos é: {:.2f}".format(media))