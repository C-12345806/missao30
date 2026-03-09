def verifica_situacao(media):
    if media >= 7:
        situacao = "Aprovado"
    elif media <= 5:
        situacao = "Reprovado"
    else:
        situacao = "Recuperação"
    return situacao


def mostrar_resultado(alunos):
    print("\n=== RESULTADO FINAL ===\n")
    for aluno in alunos:
        print("Aluno:", aluno[0])
        print("Nota 1:", aluno[1])
        print("Nota 2:", aluno[2])
        print("Nota 3:", aluno[3])
        print("Média:", round(aluno[4], 2))
        print("Situação:", aluno[5])
        print("------------------------------")


def calcula_media(notas):
    return (notas[0] + notas[1] + notas[2]) / 3


def main():
    alunos = []

    quantidade_alunos = int(input("Quantidade de alunos: "))

    if quantidade_alunos < 3:
        print("Mínimo de 3 alunos. Reinicie.")
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

        media = calcula_media(notas)
        situacao = verifica_situacao(media)

        alunos.append([nome, notas[0], notas[1], notas[2], media, situacao])

    print("\nTotal de alunos:", len(alunos))

    mostrar_resultado(alunos)

main()
