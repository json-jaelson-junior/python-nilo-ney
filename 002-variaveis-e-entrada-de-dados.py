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