# ==============================================
# Exercício 5: Calculando Média de Notas
# ==============================================

def calcular_media():
    """
    Função que recebe três notas do usuário e calcula a média.
    Inclui validação e saída organizada para portfólio.
    """

    print("=== Calculadora de Média de Notas ===\n")

    notas = []

    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite a nota {i} (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("⚠️ Nota inválida! Digite um valor entre 0 e 10.")
            except ValueError:
                print("⚠️ Entrada inválida! Digite apenas números.")

    media = sum(notas) / len(notas)

    print(f"\nAs notas informadas foram: {notas}")
    print(f"A média das notas é: {media:.2f}")

if __name__ == "__main__":
    calcular_media()