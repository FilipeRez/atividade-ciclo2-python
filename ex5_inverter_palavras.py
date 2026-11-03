# Exercicio 5 - Recebe uma frase e retorna a frase com as letras de cada palavra invertidas
# Ex.: "Ola mundo" -> "alO odnum"


def inverter_palavras(frase):
    palavras = frase.split(" ")
    invertidas = [palavra[::-1] for palavra in palavras]
    return " ".join(invertidas)


if __name__ == "__main__":
    frase = input("Digite uma frase: ")
    print(inverter_palavras(frase))
