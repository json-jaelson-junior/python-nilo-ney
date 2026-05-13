"""
### CAPÍTULO 4 ###

Condições - Estruturas aninhadas

Testando os comandos que o autor pediu nas páginas 126, 127 e 128:
"""

### Programa 4.7: Conta de telefone com três faixas de preço

minutos = int(input("Quantos minutos você utilizou esse mês: "))

if minutos < 200:
    preco = 0.20

else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15

print(f"Você vai pagar este mês: R$ {minutos * preco:6.2f}")

### Programa 4.8: Categoria x preço

categoria = int(input("Digite a categoria do produto: "))

if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print("Categoria inválida, digite um valor entre 1 e 5!")
                    preco = 0

print(f"O preço do produto é: R$ {preco:6.2f}")

"""
### EXERCÍCIO ###

Exercício 4.9 - Rastreie o Programa 4.8. Compare seu resultado ao apresentado na Tabela 4.2.
"""

# Resolução do exercício:

print("Os resultados de fato batem.")