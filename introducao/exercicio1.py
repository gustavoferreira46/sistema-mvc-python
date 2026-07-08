soma = 0
total = 0
for i in range(1,6):
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    soma += numero
    total += 1
media = soma / total
print(f"A média dos números digitados é: {media:.2f}")
