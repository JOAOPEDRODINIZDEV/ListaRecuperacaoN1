notas = []  

for i in range(1, 11):
    n = float(input("Digite a nota do aluno: "))
    notas.append(n)  

soma = sum(notas) 
media = soma / len(notas) 

print("A média dos alunos é: {}".format(media))