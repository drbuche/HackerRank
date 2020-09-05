# Problem : https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
# Score : 10 points(MAX)

def operators(a, b):
    """
    :param a, b: Recebe 2 valores inteiros.
    :return: Imprime na tela (separando por uma quebra de linha com sep='\n') a soma, diferença e produto.
    """
    print((a + b), (a - b), (a * b), sep='\n')


operators(int(input()), int(input()))  # Executa a função tendo como parametro 2 inteiros
