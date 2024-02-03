def menu():
    print("1. Adicionar um ou mais filmes")
    print("2. Mostrar a lista de filmes")
    print("3. Listar filmes por genero")
    print("4. Listar filmes de um ator")
    print("5. Remover um ou mais filmes")
    print("6. Sair")


def adicionar_dados(
    filme: str, genero: str, nome_ator: tuple, nota_filme: float, filme_tuplas: tuple
):
    dados_filme = (filme, genero, nome_ator, nota_filme)
    return filme_tuplas + (dados_filme,)


def listar_filmes(filme_tuplas: tuple):
    for filme, genero, nome_ator, nota_filme in filme_tuplas:
        print(
            f"Filme: {filme}, Genero: {genero}, Atores: {', '.join(nome_ator)}, Nota do filme: {nota_filme}"
        )


def listar_por_generos(genero_desejado: str, filme_tuplas: tuple):
    possui_filme = False
    print(f"filmes do genero {genero_desejado}: ")
    for filme, genero, nome_ator, nota_filme in filme_tuplas:
        if genero.lower() == genero_desejado.lower():
            print(
                f"Filme: {filme}, Genero: {genero}, Atores: {nome_ator}, Nota: {nota_filme:.2f}"
            )
            possui_filme = True
    if not possui_filme:
        print(f"genero {genero_desejado} não encontrado")
    print("\n")


def listar_filmes_por_ator(ator_procurado: str, filme_tuplas: tuple):
    possui_ator = False
    ator_procurado = ator_procurado.lower()
    print(f"filmes feitos pelo ator {ator_procurado}: ")
    for filme, genero, nome_ator, nota_filme in filme_tuplas:
        for ator in nome_ator:
            if ator_procurado == ator.lower():
                print(
                    f"Filme: {filme}, Genero: {genero}, Atores: {nome_ator}, Nota: {nota_filme:.2f}"
                )
                possui_ator = True
                break
    if not possui_ator:
        print(f"Ator {ator_procurado} não encontrado.")
    print("\n")


def remover_filmes(filme: str, filme_tuplas: tuple):
    filmes_encontrados = False
    novo_filme_tuplas = ()
    for filmes, genero, nome_ator, nota_filme in filme_tuplas:
        if filmes.lower() == filme.lower():
            print(
                f"Filme: {filmes}, Genero: {genero}, Atores: {nome_ator}, Nota: {nota_filme:2f}"
            )
            filmes_encontrados = True
        else:
            novo_filme_tuplas += ((filmes, genero, nome_ator, nota_filme),)
    return filmes_encontrados, novo_filme_tuplas


def main():
    menu()
    filme_tuplas = ()
    user_input = input("Escolha uma das opções acima: ")
    while True:
        match user_input:
            case "1":
                inserir_novo_filme = "s"
                while inserir_novo_filme == "s":
                    nome_filme = input("Insira o nome do filme: ")
                    genero_filme = input(f"Insira o genero do filme {nome_filme}: ")
                    atores_do_filme = ()
                    inserir_novo_ator = "s"
                    while inserir_novo_ator == "s":
                        nome_ator = input(
                            f"Insira o nome de um ator/atriz do filme {nome_filme}: "
                        )
                        atores_do_filme += (nome_ator,)
                        inserir_novo_ator = input(
                            "Deseja adicionar outro ator/atriz para este filme? (s/n) "
                        )
                    nota_filme = float(
                        input(f"Insira uma nota para o filme {nome_filme}: ")
                    )
                    filme_tuplas = adicionar_dados(
                        nome_filme,
                        genero_filme,
                        atores_do_filme,
                        nota_filme,
                        filme_tuplas,
                    )
                    inserir_novo_filme = input("Deseja adicionar outro filme? (s/n)")
                menu()
                user_input = input("Escolha uma das opções acima: ")
            case "2":
                if not filme_tuplas:
                    print("Não há filmes cadastrados.")
                else:
                    listar_filmes(filme_tuplas)
                menu()
                user_input = input("Escolha uma das opções acima: ")

            case "3":
                if not filme_tuplas:
                    print("Não há filmes cadastrados.")
                    menu()
                    user_input = input("Escolha uma das opções acima: ")
                    continue
                listar_genero = input("Qual gênero de filme você deseja procurar? ")
                listar_por_generos(listar_genero, filme_tuplas)
                menu()
                user_input = input("Escolha uma das opções acima: ")

            case "4":
                if not filme_tuplas:
                    print("Não há filmes cadastrados.")
                    menu()
                    user_input = input("Escolha uma das opções acima: ")
                    continue
                inserir_novo_ator = "s"
                while inserir_novo_ator == "s":
                    ator_procurado = input(
                        "Digite o nome do ator/atriz que deseja procurar: "
                    )
                    listar_filmes_por_ator(ator_procurado, filme_tuplas)
                    inserir_novo_ator = input(
                        "Deseja procurar outro ator/atriz? (s/n) "
                    ).lower()
                menu()
                user_input = input("Escolha uma das opções acima: ")

            case "5":
                if not filme_tuplas:
                    print("Não há filmes cadastrados.")
                    menu()
                    user_input = input("Escolha uma das opções acima: ")
                    continue
                removendo_filme = "s"
                while removendo_filme == "s":
                    filme_removido = input(
                        "Digite o nome do filme que deseja remover: "
                    )
                    filme_encontrado, filme_tuplas = remover_filmes(
                        filme_removido, filme_tuplas
                    )
                    if filme_encontrado:
                        print(f"O filme {filme_removido} foi removido com sucesso.")
                    else:
                        print(f"O filme {filme_removido} não foi encontrado.")
                    removendo_filme = input("Deseja remover outro filme? (s/n) ")
                menu()
                user_input = input("Escolha uma das opções acima: ")

            case "6":
                break

            case _:
                print("Opção inválida.")
                user_input = input("Escolha uma das opções acima: ")


if __name__ == "__main__":
    main()
