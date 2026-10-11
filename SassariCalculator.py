def ler_numero(pergunta):
    """Lê um número aceitando vírgula ou ponto como separador decimal."""
    while True:
        texto = input(pergunta).strip().replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("Valor inválido. Digite apenas números (ex.: 1500 ou 2,5).")


def formata(valor):
    """Formata no padrão brasileiro: 1.234,56"""
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


optionJ = input("Você deseja fazer o cálculo de Juros Simples (S) ou Juros Compostos? (C) ")

match optionJ:
    case 'S' | 's':
        print("Você selecionou 'Juros Simples', informe os valores a seguir...")
        cap = ler_numero("Qual o valor do Capital? ")
        txJ = ler_numero("Qual o valor da Taxa de Juros (%)? ")
        resTX = txJ / 100
        time = ler_numero("Qual o tempo? ")
        resJr = cap * resTX * time
        mont = cap * (1 + resTX * time)

        print(f"O valor dos juros é de {formata(resJr)}")
        print(f"O valor do montante é de {formata(mont)}")

    case 'C' | 'c':
        print("Você selecionou 'Juros Compostos', informe os valores a seguir...")
        cap = ler_numero("Qual o valor do Capital? ")
        txJ = ler_numero("Qual o valor da Taxa de Juros (%)? ")
        resTX = txJ / 100
        time = ler_numero("Qual o tempo? ")
        resJc = cap * pow(1 + resTX, time)
        Jr = resJc - cap

        print(f"O valor do montante é de {formata(resJc)}")
        print(f"O valor dos juros é de {formata(Jr)}")

    case _:
        print("Opção inválida. Digite S para Juros Simples ou C para Juros Compostos.")

input("\nPressione Enter para sair...")