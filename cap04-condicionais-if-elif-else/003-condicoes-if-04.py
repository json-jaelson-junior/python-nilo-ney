"""
### CAPÍTULO 4 ###

Condições - If 04

Testando os comandos que o autor pediu nas páginas 123 e 124:
"""

### If

# If nada mais é do que um "se"; se a condição for verdadeira, faça tal coisa

### Programa 4.4 - Cálculo da mensalidade de um plano de celular da operadora Tchau

plano = input("Qual é o seu plano de celular? ")

if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.20            # <- Bloco 1
    preco = 50

if plano == "falomuito":
    minutos_no_plano = 500
    extra = 0.15            # <- Bloco 2
    preco = 99

if plano != "falopouco" and plano != "falomuito":
    print("Não conheço esse plano")                 # <- Bloco 3

if plano == "falopouco" or plano == "falomuito":
    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar:")                                            # <- Bloco 4
    print(f"Preço do plano  R$ {preco:10.2f}")
    suplemento = 0

    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
    
    print(f"Suplemento      R$ {suplemento:10.2f}")                   # <- Bloco 5
    print(f"Total           R$ {preco + suplemento:10.2f}")