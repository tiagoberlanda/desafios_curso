#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
def sequencia_fibonacci(n):
    fibonacci = [0, 1]  # Inicializa a sequência de Fibonacci com os dois primeiros elementos

    while len(fibonacci) < n:
        proximo_elemento = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_elemento)

    return fibonacci[:n]

def main():
    try:
        n = int(input('Digite um número inteiro N: '))
        if n <= 0:
            print("Digite um número inteiro positivo maior que zero.")
        else:
            resultado = sequencia_fibonacci(n)
            print("Os primeiros", n, "elementos da Sequência de Fibonacci são:")
            print(resultado)

    except ValueError:
        print("Digite um número inteiro válido.")

if __name__ == "__main__":
    main()

