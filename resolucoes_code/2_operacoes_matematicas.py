# ==============================================
# Exercício 2: Repetindo Textos
# ==============================================

def operacoes_matematicas():
    """
    Função que recebe dois números do usuário e realiza operações matemáticas básicas:
    soma, subtração, multiplicação e divisão.
    Inclui validação e saída organizada para portfólio.
    """

    print("=== Calculadora Simples ===\n")

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("⚠️ Entrada inválida! Digite apenas números.")

    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2

    if num2 != 0:
        divisao = num1 / num2
    else:
        divisao = "Não é possível dividir por zero!"

    print("\n=== Resultados ===")
    print(f"Soma: {num1} + {num2} = {soma}")
    print(f"Subtração: {num1} - {num2} = {subtracao}")
    print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
    print(f"Divisão: {num1} / {num2} = {divisao}")

if __name__ == "__main__":
    operacoes_matematicas()