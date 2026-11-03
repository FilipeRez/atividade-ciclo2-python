# Exercicio 3 - Le 3 numeros inteiros e mostra o menor deles


def menor_de_tres(n1, n2, n3):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor


if __name__ == "__main__":
    n1 = int(input("Digite o 1o numero: "))
    n2 = int(input("Digite o 2o numero: "))
    n3 = int(input("Digite o 3o numero: "))
    print(f"O menor numero e {menor_de_tres(n1, n2, n3)}.")
