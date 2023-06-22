
def calcular_desconto():
    valor = float(input("Qual é o valor do produto? "))
    idade = int(input("Qual é a sua idade? "))
    if idade > 21:
        desconto = valor * (15/100)
        novo_valor = valor - desconto
    else:
        desconto = valor * (10/100)
        novo_valor = valor - desconto
        
    print("O Desconto é de: {}".format(desconto))
    print("O valor Com Desconto: {}".format(novo_valor))
calcular_desconto()
