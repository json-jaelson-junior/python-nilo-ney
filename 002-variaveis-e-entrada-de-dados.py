#VARIÁVEIS NUMÉRICAS

#Exercício 3.1
#numeros_inteiros = 5, -2, 100
#numeros_ponto_flutuante = 5.0, 4.3, 1.333

#BINÁRIA - OCTAL - HEXADECIMAL

#a = 0b11
#b = 0x11
#c = 0o11

#print(a, b, c)

#VARIÁVEIS DO TIPO LÓGICO

#Operadores relacionais e Boolean:

#True or False
#Igualdade = ==
#Maior que = >
#Menor que = <
#Diferente = !=
#Maior ou igual = >=
#Menos ou igual = <=

#a = 1
#b = 5
#c = 2
#d = 1

#a == b #False
#b > a #True
#a < b #True
#a == d #True
#b >= a #True
#c <= b #True
#d != a #False
#d != b #True

#nota = 8
#media = 7
#aprovado = nota >= media
#print(aprovado)

#Exercício 3.2

#a = 4
#b = 10
#c = 5.0
#d = 1
#f = 5

#a == c #False
#a < b #True
#d > b #False
#c != f #False
#a == b #False
#c < d #False
#b > a #True
#c >= f #True
#f >= c #True
#c <= c #True
#c <= f #True

#OPERADORES LÓGICOS (not, and, or)

#not

#print(not True) #False
#print(not False) #True

#and

#print(True and True) #True
#print(True and False) #False
#print(False and True) #False
#print(False and False) #False

#or

#print(True or True) #True
#print(True or False) #True
#print(False or True) #True
#print(False or False) #False

#Exercício 3.3

#a = True
#b = False
#c = True

#a and a #True
#b and b #False
#not c #False
#not b #True
#not a #False
#a and b #False
#b and c #False
#a or c #True
#b or c #True
#c or a #True
#c or b #True
#c or c #True
#b or b #False

#EXPRESSÕES LÓGICAS

#Ordem das expressões: not > and > or

#Exercício 3.4

#salario = float(1900)
#paga_importo = salario > 1200

#print(paga_importo)

#Exercício 3.5

#a1 = 1
#b1 = 2
#c1 = True
#d1 = False

#print(a1 > b1 and c1 or d1) #False

#a2 = 10
#b2 = 3
#c2 = False
#d2 = False

#print(a2 > b2 and c2 or d2) #False

#a3 = 5
#b3 = 1
#c3 = True
#d3 = True

#print(a3 > b3 and c3 or d3) #True

#Exercício 3.6

#materia1 = float(7)
#materia2 = float(8)
#materia3 = float(6.5)

#media = (materia1 + materia2 + materia3) / 3 > 7

#print(media) #True

#VARIÁVEIS STRING

#Verificando o tamanho de uma string

#a = len("A") #1
#b = len("AB") #2
#c = len("") #0
#d = len("O rato roeu a roupa") #19

#print(a, b, c, d)

#Identificando um caractere pelo índice

#a = "ABCDEF"

#print(a[0]) #A
#print(a[1]) #B
#print(a[5]) #F
#print(len(a)) #6
#print(a[6]) #Dará erro

#Operações com strings

#Concatenação

#s = "ABC"

#print(s + "C")
#print(s + "D" * 4)
#print("X" + "-" * 10 + "X")
#print(s + "x4 = " + s * 4)

#nome = "Tião"
#idade = 10
#print(nome + idade) #Essa forma de concatenação só pode ser utilizada com strings

#Composição

#idade = 22

#print("[%d]" % idade)
#print("[%03d]" % idade)
#print("[%3d]" % idade)
#print("[%-3d]" % idade)

#Casas decimais

#valor = 7

#print("%5f" % valor)
#print("%5.2f" % valor)
#print("%10.2f" % valor)

#Nesse ponto do livro, o autor aborda um pouco mais o uso de composição e .format, por estarem em desuso, optei por apenas ler o livro.
#Posso me aprofundar futuramente, tendo em vista que muitas empresas ainda podem utilizar esses formatos.
#Mas por enquanto, focarei em f-strings.

#nome = "João"
#idade = 22
#grana = 51.34

#print(f"{nome} tem {idade} anos e R$ {grana} no bolso.")
#print(f"{nome:12} tem {idade:3} anos e R$ {grana:5.2f} no bolso.")
#print(f"{nome:12} tem {idade:03} anos e R$ {grana:5.2f} no bolso.")
#print(f"{nome:<12s} tem {idade:<3} anos e R$ {grana:5.2f} no bolso.")

#Fatiamento de strings

#s = "ABCDEFGHI"

#print(s[0:2])
#print(s[1:2])
#print(s[2:4])
#print(s[0:5])
#print(s[1:8])

#De um índice ao início ou fim
#print(s[:2])
#print(s[1:])
#print(s[:])

#Negativo
#print(s[0:-2])
#print(s[-1:])
#print(s[-5:7])
#print(s[-2:-1])
#print(s[::-1])
#print(s[::2])

#SEQUÊNCIAS E TEMPO

#divida = 0
#compra = 100
#divida = divida + compra
#compra = 200
#divida = divida + compra
#compra = 300
#divida = divida + compra
#compra = 0

#print(divida) #600

#O código é executado de cima para baixo, devemos lembrar que os valores das variáveis serão alterados nessa ordem.

#ENTRADA# DE DADOS

#x = inpu#t("Digite um número: ")

#print(x)#

#nome = input("Digite seu nome: ")

#print(f"Você digitou {nome}")
#print(f"Olá, {nome}!")

#Conversão da entrada de dados

#anos = int(input("Anos de serviço: "))
#valor_por_ano = float(input("Valor por ano: "))
#bonus = anos * valor_por_ano

#print(f"Bônus de R$ {bonus:5.2f}")

#Exercício 3.7

#num1 = int(input("Digite um número: "))
#num2 = int(input("Digite outro número: "))
#soma = num1 + num2

#print(f"A soma dos dois números é {soma}")

#Exercício 3.8

#valor_em_metros = int(input("Digite o valor em metros: "))
#metros_para_milimetros = valor_em_metros * 1000

#print(f"O valor de {valor_em_metros} metros em milímetros é de {metros_para_milimetros}.")

#Exercício 3.9

#dias = int(input("Digite a quantidade de dias: "))
#horas = int(input("Digite a quantidade de horas: "))
#minutos = int(input("Digite a quantidade de minutos: "))
#segundos = int(input("Digite a quantidade de segundos: "))

#conversao_para_segundos = dias * (24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

#print(f"O total de segundos é {conversao_para_segundos} segundos.")

#Exercício 3.10

#salario = float(input("Digite o salário: "))
#percentual_de_aumento = float(input("Digite a porcentagem do aumento: "))
#valor_do_aumento = (salario * percentual_de_aumento / 100)
#novo_salario = salario + (salario * percentual_de_aumento / 100)

#print(f"O aumento no salário foi de R$ {valor_do_aumento:.2f}. O valor do novo salário é R$ {novo_salario:.2f}")

#Exercício 3.11

#preco_da_mercadoria = float(input("Digite o preço da mercadoria: "))
#percentual_de_desconto = float(input("Digite a porcentagem do desconto: "))
#valor_do_desconto = (preco_da_mercadoria * percentual_de_desconto / 100)
#valor_final = preco_da_mercadoria - (preco_da_mercadoria * percentual_de_desconto / 100)

#print(f"O valor do desconto é de R$ {valor_do_desconto:.2f}. O valor da mercadoria ficou R$ {valor_final:.2f}.")