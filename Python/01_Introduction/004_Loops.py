# Problem : https://www.hackerrank.com/challenges/python-loops/problem
# Score : 10 points(MAX)

def loop(n):
    """
    :param n: Recebe um numero.
    :return: Retorna os quadrados de 0 até (n-1).
    """
    [print(x**2) for x in range(n)]


loop(int(input()))  # Executa a função tendo como parametro um inteiro
