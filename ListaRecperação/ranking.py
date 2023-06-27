
livros = {}

qtd_livros = int(input("Digite a Quantidade de Livros: "))

for i in range(qtd_livros):
    livro = input(f"\nDigite o {i+1}° nome do livro: ")
    posicao = int(input("\nDigite a posição do livro: "))
    livros[posicao] = livro

print("\nRanking Dos Livros")

for indice, livro in sorted(livros.items()):
    print(f"{indice} - {livro}")
    