# Exercicio 1 - Converte idade em dias para anos, meses e dias
# Considera ano = 365 dias e mes = 30 dias


def converter_idade(total_dias):
    anos = total_dias // 365
    resto = total_dias % 365
    meses = resto // 30
    dias = resto % 30
    return anos, meses, dias


if __name__ == "__main__":
    total = int(input("Digite a idade em dias: "))
    anos, meses, dias = converter_idade(total)
    print(f"{total} dias equivalem a {anos} ano(s), {meses} mes(es) e {dias} dia(s).")
