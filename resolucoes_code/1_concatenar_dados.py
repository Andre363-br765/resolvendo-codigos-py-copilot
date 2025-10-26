# ==============================================
# Exercício 1: Concatenando Dados
# ==============================================

def concatenar_dados():
    """
    Função que recebe dois dados do usuário e os concatena em uma única string.
    """

    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")

    resultado = f"{dado1}{dado2}"

    print("\n=== Resultado da Concatenação ===")
    print(f"{dado1} + {dado2} = {resultado}")

if __name__ == "__main__":
    concatenar_dados()
