# ==============================================
# Exercício 4: Verificando Números Pares e Ímpares
# ==============================================

def par_ou_impar():
    """
    Função que recebe um número inteiro do usuário e verifica se ele é par ou ímpar.
    Inclui validação de entrada e saída organizada para portfólio.
    """

    print("=== Verificador de Números Pares e Ímpares ===\n")

    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("⚠️ Entrada inválida! Digite apenas números inteiros.")

    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "ímpar"

    print(f"\nO número {numero} é {resultado}.")

if __name__ == "__main__":
    par_ou_impar()
