"""
### CAPÍTULO 3 ###

Variáveis string - (len e índices)

Testando os comandos que o autor pediu nas páginas 101 e 102:
"""

### Representação de uma string

print("Uma string é o conteúdo que fica dentro de aspas, sejam simples ou duplas.")

### Tamanho da string

len("A") # 1
len("AB") #2
len("") #0
len("O rato roeu a roupa") #19

### Índices de uma string

print("Toda string começa pelo índice 0; 0 = A, 1 = B, 2 = C, 3 = D ...")

"""
    012345678 <- Índice
    ABCDEFGHI <- Conteúdo
"""

# Selecionando um caractere pelo índica

a = "ABCDEF"

print(a[0]) #A
print(a[1]) #B
print(a[5]) #F
print(len(a)) #6
print(a[6]) #Dará erro, pois o índice 6 não existe