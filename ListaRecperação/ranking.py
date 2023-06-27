livros = {}

for i in range(1, 5):
    livro = input(f"Digite o {i} nome do livro: ")
    livros[i] = livro

print("\nRanking de Mais Vendido")

for indice, livro in livros.items():
    print(f"{indice} - {livro}")