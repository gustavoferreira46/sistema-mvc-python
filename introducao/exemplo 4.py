    # Apenas escrevendo os numeros de 1 a 10
for i in range(1, 10):
  print(i)
valor = int(input("Digite um valor: "))
fatorial = 1
for i in range(1, valor + 1):
   fatorial *= i
   print(f"O fatorial de {valor} é {fatorial}")