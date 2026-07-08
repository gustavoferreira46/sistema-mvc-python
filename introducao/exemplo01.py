numero1 = int(input("digite um valor: "))
numero2 = int(input("digite um valor: "))

resposta = numero1 + numero2
print("resposta", resposta)

numero1, numero2 = numero2, numero1 

print("numero 1: ", numero1)
print("numero 2: ", numero2)