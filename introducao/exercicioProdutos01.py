from colorama import Fore, Style, init

init(autoreset=True)

produtos = [

    {"ID": 1, "nome": "teclado", "valor_uni": 50.00, "estoque": 3},
    {"ID": 2, "nome": "fone", "valor_uni": 200.00, "estoque": 10},
    {"ID": 3, "nome": "mouse", "valor_uni": 30.00, "estoque": 50},
    {"ID": 4, "nome": "rtx 5090", "valor_uni": 550.00, "estoque": 2},

]

print("ID | Nome | Valor_Uni | Estoque")

for produto in produtos:

    valor_estoque = produto["valor_uni"] * produto["estoque"]

    if produto["estoque"] < 10:
        print(Fore.RED + "Estoque baixo, reabastecimento necessário")

    elif produto["estoque"] < 50:
        print(Fore.YELLOW + "Atenção, monitorar estoque")

    else:
        print(Fore.GREEN + "Tudo OK, estoque adequado")

    print(
        produto["ID"],
        produto["nome"],
        produto["estoque"],
        valor_estoque,
       
    )