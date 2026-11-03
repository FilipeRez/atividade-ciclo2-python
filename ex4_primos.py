# Exercicio 4 - Funcao que retorna True se o numero for primo, False caso contrario
# Testa os numeros de 1 a 100


def eh_primo(n):
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


if __name__ == "__main__":
    for numero in range(1, 101):
        print(f"{numero}: {eh_primo(numero)}")

    primos = [n for n in range(1, 101) if eh_primo(n)]
    print(f"\nPrimos de 1 a 100 ({len(primos)} no total): {primos}")
