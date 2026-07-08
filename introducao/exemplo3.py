while True:
    try:
        valor1 = int(input("Digite o primeiro valor: "))
        break

    except ValueError:
        print("Valor invalido! Por favor, digite um numero inteiro.")

    except KeyboardInterrupt:
        print("\nOperacao cancelada pelo usuario.")
        exit(1)

while True:
    try:
        valor2 = int(input("Digite o segundo valor: "))
        break

    except ValueError:
        print("Valor invalido! Por favor, digite um numero inteiro.")

    except KeyboardInterrupt:
        print("\nOperacao cancelada pelo usuario.")
        exit(1)

print("Selecione uma opcao:")
print("1 adicao")
print("2 subtracao")
print("3 multiplicacao")
print("4 divisao")

opcao = input("Digite a opcao desejada: ")

resultado = None

match opcao:
    case "1":
        resultado = valor1 + valor2

    case "2":
        resultado = valor1 - valor2

    case "3":
        resultado = valor1 * valor2

    case "4":
        try:
            resultado = valor1 / valor2
        except ZeroDivisionError:
            print("Erro: divisao por zero nao e permitida.")

    case _:
        print("Opcao invalida")