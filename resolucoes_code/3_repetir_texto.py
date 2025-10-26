# ==============================================
# Exercício 3: Operações Matemáticas Simples
# ==============================================

def repetir_texto():
    """
    Função que recebe uma string e um número inteiro do usuário
    e retorna a string repetida o número de vezes informado.
    Inclui validação e exemplos divertidos para portfólio.
    """

    print("=== Bem-vindo ao Repetidor de Textos! ===\n")

    texto = input("Digite um texto qualquer (ex: 'Hello', 'XD', 'Oink'): ")
    
    while True:
        try:
            vezes = int(input("Digite o número de repetições (maior que 0): "))
            if vezes <= 0:
                print("⚠️ Por favor, digite um número maior que zero.")
                continue
            break
        except ValueError:
            print("⚠️ Entrada inválida! Digite apenas números inteiros.")

    resultado = (texto + " ") * vezes

    print("\n=== Resultado da Repetição ===")
    print(f"O texto '{texto}' repetido {vezes} vezes fica:\n{resultado}")

if __name__ == "__main__":
    repetir_texto()
