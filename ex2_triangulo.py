# Exercicio 2 - Verifica se a, b, c formam um triangulo e calcula a area
# Um triangulo existe quando cada lado e menor que a soma dos outros dois.
# A area e calculada pela formula de Heron.
import math


def forma_triangulo(a, b, c):
    return a < b + c and b < a + c and c < a + b


def area_triangulo(a, b, c):
    s = (a + b + c) / 2  # semiperimetro
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == "__main__":
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))

    if forma_triangulo(a, b, c):
        print(f"Os valores formam um triangulo. Area = {area_triangulo(a, b, c):.2f}")
    else:
        print(f"Os valores {a}, {b} e {c} nao formam um triangulo.")
