"""
### CAPÍTULO 4 ###

Condições - If 02

Testando os comandos que o autor pediu nas páginas 120 e 121:
"""

### If

# If nada mais é do que um "se"; se a condição for verdadeira, faça tal coisa

### Programa 4.2: Carro novo ou velho, dependendo da idade

idade = int(input("Digite a idade do seu carro: "))

if idade <= 3:
    print("Seu carro é novo") #1

if idade > 3:
    print("Seu carro é velho") #2

"""
### EXERCÍCIO ###

Exercício 4.2 - Escreva um programa que pergunte a velocidade do carro de um usuário.

Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
"""

# Resolução do exercício:

velocidade = int(input("Digite a velocidade do carro: "))
calculo_da_multa = (velocidade % 80) * 5
km_alem_do_permitido = (velocidade % 80)

if velocidade > 80:
    print(f"Você foi multado em R$ {calculo_da_multa}, pois está a {km_alem_do_permitido} km/h além do permitido.")

if velocidade <= 80:
    print(f"A sua velocidade é de {velocidade} km/h, você pode passar e não foi multado.")