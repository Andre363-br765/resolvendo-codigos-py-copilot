# ==============================================
# Exercício 6: Verificando Palíndromos
# ==============================================

def verificar_palindromo():
    """
    Função que recebe uma palavra do usuário e verifica se é um palíndromo.
    Inclui validação e saída organizada para portfólio.
    """

    print("=== Verificador de Palíndromos ===\n")

    palavra = input("Digite uma palavra: ").strip().lower()

    if palavra == palavra[::-1]:
        resultado = "é um palíndromo!"
    else:
        resultado = "não é um palíndromo."

    print(f"\nA palavra '{palavra}' {resultado}")

if __name__ == "__main__":
    verificar_palindromo()
