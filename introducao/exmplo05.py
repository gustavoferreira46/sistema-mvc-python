#Exemplo de lista 

lista = [10, 20, 30, 40, 50]

lista.append(60)  
#print(lista)
lista[3] = 90
#print(lista)


#exemplo de tupla

tupla = (10, 20, 30, 40, 50)
#print(tupla)

#exemplo de dicionario

dicionario = {
    "RA" : "2345678",
    "Nome" : "gabriel pensador",
    "Idade" : 20,
    "Curso" : "TDS"
}

#print(dicionario["Nome"])
print("imprime a lista")
for item in lista:
    print(item)

print("imprime a tupla")
for item in tupla:
    print(item)

print("imprime o dicionario versao 1: ")
for chave in dicionario:
    print(chave, ":", dicionario[chave])

print("imprime o dicionario versao 2: ")
for chave, valor in dicionario.items():
    print(chave, ":", valor)