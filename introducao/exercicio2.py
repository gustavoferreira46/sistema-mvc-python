from colorama import Fore, init, Back, Style
init(autoreset=True)

def ler_dados():
    while True:  
        try:
            valor = int(input("Digite um número inteiro: "))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

total_pares = 0
total_impares = 0

valor = ler_dados()

while valor != 0:
    if valor % 2 == 0:
        total_pares += 1
    else:
        total_impares += 1
    valor = ler_dados()
print(Fore.GREEN + "Total de números pares: ", Fore.BLUE + str(total_pares))
print(Fore.GREEN + "Total de números ímpares: ", Fore.RED + str(total_impares))
