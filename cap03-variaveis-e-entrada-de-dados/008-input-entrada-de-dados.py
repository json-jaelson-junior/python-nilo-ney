"""
### CAPÍTULO 3 ###

Input - Entrada de Dados

Testando os comandos que o autor pediu nas páginas 112 e 113:
"""

### Utilizando o input

# A função input é utilizada para solicitar dados do usuário

# Exemplo 1

x = input("Digite um número: ") # Pede um número ao usuário

print(x) # Será exibido o número digitado pelo usuário

# Exemplo 2

nome = input("Digite seu nome: ") # Usuário digita "Jaelson"

print(f"Você digitou {nome}") # Você digitou Jaelson
print(f"Olá, {nome}!") # Olá, Jaelson!

### Conversão da entrada de dados

# Todo input é uma string, por isso, quando um número for solicitado, devemos converter a entrada para int ou float

anos = int(input("Anos de serviço: ")) # Converte para um número inteiro
valor_por_ano = float(input("Valor por ano: ")) # Converte para um número com ponto flutuante
bonus = anos * valor_por_ano

print(f"Bônus de R$ {bonus:5.2f}")

# Caso a conversão não seja feita, os números serão concatenados

"""
### EXERCÍCIOS ###

Exercício 3.7 - Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.
"""

# Resolução do exercício:

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = num1 + num2

print(f"A soma dos dois números é {soma}")

"""
Exercício 3.8 - Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
"""

# Resolução do exercício:

valor_em_metros = float(input("Digite o valor em metros: "))
metros_para_milimetros = valor_em_metros * 1000

print(f"O valor de {valor_em_metros} metros em milímetros é de {metros_para_milimetros}.")

"""
Exercício 3.9 - Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.

Calcule o total em segundos.
"""

# Resolução do exercício:

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
conversao_para_segundos = dias * (24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print(f"O total de segundos é {conversao_para_segundos} segundos.")

"""
Exercício 3.10 - Faça um programa que calcule o aumento de um salário.

Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
"""

# Resolução do exercício:

salario = float(input("Digite o salário: "))
percentual_de_aumento = float(input("Digite a porcentagem do aumento: "))
valor_do_aumento = (salario * percentual_de_aumento / 100)
novo_salario = salario + (salario * percentual_de_aumento / 100)

print(f"O aumento no salário foi de R$ {valor_do_aumento:.2f}. O valor do novo salário é R$ {novo_salario:.2f}")

"""
Exercício 3.11 - Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.

Exiba o valor do desconto e o preço a pagar.
"""

# Resolução do exercício:

preco_da_mercadoria = float(input("Digite o preço da mercadoria: "))
percentual_de_desconto = float(input("Digite a porcentagem do desconto: "))
valor_do_desconto = (preco_da_mercadoria * percentual_de_desconto / 100)
valor_final = preco_da_mercadoria - (preco_da_mercadoria * percentual_de_desconto / 100)

print(f"O valor do desconto é de R$ {valor_do_desconto:.2f}. O valor da mercadoria ficou R$ {valor_final:.2f}.")

"""
Exercício 3.12 - Escreva um programa que calcule o tempo de uma viagem de carro.

Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
"""

# Resolução do exercício:

distancia_trajeto_km = float(input("Digite quantos KM de distância terá a viagem: "))
velocidade_media_kmh = float(input("Digite a velocidade média do carro em KM: "))
tempo_estimado = distancia_trajeto_km / velocidade_media_kmh
conversao_horas = int(tempo_estimado)
sobra_horas = tempo_estimado - conversao_horas
conversao_minutos = int(sobra_horas * 60)

print(f"Dirigindo a {velocidade_media_kmh} KM/h, você chegará ao seu destino em {conversao_horas}h{conversao_minutos:02d}m.")

"""
Exercício 3.13 - Escreva um programa que converta uma temperatura digitada em °C em °F. 

A fórmula para essa conversão é: F = (9 x C / 5) + 32
"""

# Resolução do exercício:

celcius = float(input("Digite a temperatura em Celcius: "))
celcius_para_fahrenheit = (9 * celcius / 5) + 32

print(f"A temperatura em Fahrenheit é de {celcius_para_fahrenheit}°.")

"""
Exercício 3.14 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
assim como a quantidade de dias pelos quais o carro foi alugado.

Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""

# Resolução do exercício:

dias_alugado = int(input("Digite a quantidade de dias que o carro foi alugado: "))
km_percorridos = float(input("Digite a quantidade de KM percorridos com o carro: "))
valor_por_km = km_percorridos * 0.15
valor_por_dia = dias_alugado * 60
valor_final_aluguel = valor_por_km + valor_por_dia

print(f"Você alugou o carro por {dias_alugado} dias e percorreu {km_percorridos} KM. O valor total a pagar é de R$ {valor_final_aluguel:.2f}.")

"""
Exercício 3.14 - Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá.

Exiba o total em dias.
"""

# Resolução do exercício:

quantidade_cigarros_dia = int(input("Digite quantos cigarros você fuma por dia: "))
anos_fumando = int(input("Digite a quantidade de anos que você já fumou: "))
total_cigarros = quantidade_cigarros_dia * (anos_fumando * 365)
dias_perdidos = (total_cigarros * 10 / 60) / 24

print(f"Você fumou {total_cigarros} cigarros no total. Por isso, já perdeu {dias_perdidos:.0f} dias de vida.")