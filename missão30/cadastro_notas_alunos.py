def main():
    alunos = []

    quantidade_alunos = int(input("Quantidade de alunos: "))

    if quantidade_alunos < 10:
        print("Mínimo de 10 alunos. Reinicie.")
        return

    for i in range(quantidade_alunos):

        nome = input("Nome: ")
        notas = []

        while len(notas) < 3:
            nota = float(input("Nota: "))
            if nota < 0 or nota > 10:
                print("Nota inválida")
                continue
            notas.append(nota)

        media = (notas[0] + notas[1] + notas[2]) / 3

        if media >= 7:
            situacao = "Aprovado"
        elif media >= 5:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        alunos.append([nome, notas[0], notas[1], notas[2], media, situacao])

    print("\nTotal de alunos:", len(alunos))

    for aluno in alunos:
        print(aluno)

main()