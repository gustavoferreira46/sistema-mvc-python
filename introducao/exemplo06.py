alunos = [
    {
        "ID" : 1,
        "Nome" : "Joãozinho",
        "Nota1" : 7.5,
        "Nota2" : 8.0
    },
    {
        "ID" : 2,
        "Nome" : "Mariazinha",
        "Nota1" : 9.0,
        "Nota2" : 9.5
    },
    {
        "ID" : 3,
        "Nome" : "Pedrinho",
        "Nota1" : 6.0,
        "Nota2" : 7.0
    }
]

pessoa = {
    "ID" : 4,
    "Nome" : "Gabriel Pensador",
    "Nota1" : 10.0,
    "Nota2" : 10.0
}
alunos.append(pessoa)
for aluno in alunos:
    print(aluno["ID"])
    print(aluno["Nome"])
    media = (aluno["Nota1"] + aluno["Nota2"]) / 2
    print(f"Media: { media:.2f}")
    print("-" * 20)