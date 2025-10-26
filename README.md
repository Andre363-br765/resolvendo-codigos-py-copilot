# Resolvendo Códigos em Python com o Github Copilot

<br>
Aprendendo Python com pequenos exercícios práticos e aproveitando sugestões do Github Copilot para escrever código de forma eficiente.

---

## 1 - Concatenando Dados 🐾

Descrição:
Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?! 

O que aprenderemos?

* Manipulação de Strings (string)
* Concatenação
* Entrada de dados
* Utilização eficiente do Github Copilot

```py
def concatenar_dados():
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")

    resultado = f"{dado1}{dado2}"

    print("\n=== Resultado da Concatenação ===")
    print(f"{dado1} + {dado2} = {resultado}")

if __name__ == "__main__":
    concatenar_dados()
```

---

## 2 - Repetindo Textos ✏️

Descrição:
Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado. 

O que aprenderemos?

* Manipulação de Strings (string)
* Números Inteiros (int)
* Múltiplas repetições
* Entrada de dados
* Aproveitar as sugestões do Github Copilot

```py
def operacoes_matematicas():
    print("=== Calculadora Simples ===\n")

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

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
```

---

## 3 - Operações Matemáticas Simples 📐

Descrição:
Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

O que aprenderemos?

* Operações Matemáticas Básicas
* Entrada de dados
* Utilização eficiente do Github Copilot

```py
def repetir_texto():
    print("=== Bem-vindo ao Repetidor de Textos! ===\n")

    texto = input("Digite um texto qualquer (ex: 'Hello', 'XD', 'Oink'): ")
    
    while True:
        try:
            vezes = int(input("Digite o número de repetições (maior que 0): "))
            if vezes <= 0:
                print("Por favor, digite um número maior que zero.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

    resultado = (texto + " ") * vezes

    print("\n=== Resultado da Repetição ===")
    print(f"O texto '{texto}' repetido {vezes} vezes fica:\n{resultado}")

if __name__ == "__main__":
    repetir_texto()
```

---

## 4 - Verificando Números Pares e Ímpares 🧮

Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

O que aprenderemos?
* Utilização de condicionais em Python (if, else) para realizar verificações.
* Introdução ao conceito de operador de módulo (%) para verificar se um número é par ou ímpar.
* Exploração do uso de uma ferramenta de IA, como o Github Copilot, para otimizar a estrutura do código.

```py
def par_ou_impar():
    print("=== Verificador de Números Pares e Ímpares ===\n")

    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "ímpar"

    print(f"\nO número {numero} é {resultado}.")

if __name__ == "__main__":
    par_ou_impar()
```
---
## 5 - Calculando Média de Notas 📚

Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. 
Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

O que aprenderemos?
* Uso de variáveis para armazenar dados fornecidos pelo usuário.
* Aplicação de operadores aritméticos (+, /) para calcular a média de um conjunto de valores.
* Prática na solicitação e manipulação de entrada do usuário.
```py
def calcular_media():
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
                    print("Nota inválida! Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite apenas números.")

    media = sum(notas) / len(notas)

    print(f"\nAs notas informadas foram: {notas}")
    print(f"A média das notas é: {media:.2f}")

if __name__ == "__main__":
    calcular_media()
```

---

## 6 - Verificando Palíndromos 🔄

Descrição: Vamos testar se uma palavra é um palíndromo?! 
Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

O que aprenderemos?
* Manipulação de strings em Python, especialmente invertendo uma string.
* Compreensão de como comparar a string original com sua versão invertida para determinar se é um palíndromo.
* Introdução ao conceito de palíndromos e sua aplicação em problemas de programação.
```py
def verificar_palindromo():
    print("=== Verificador de Palíndromos ===\n")

    palavra = input("Digite uma palavra: ").strip().lower()

    if palavra == palavra[::-1]:
        resultado = "é um palíndromo!"
    else:
        resultado = "não é um palíndromo."

    print(f"\nA palavra '{palavra}' {resultado}")

if __name__ == "__main__":
    verificar_palindromo()
```
