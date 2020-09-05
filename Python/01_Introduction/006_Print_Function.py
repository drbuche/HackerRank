# Problem : https://www.hackerrank.com/challenges/python-print/problem
# Score : 20 points(MAX)

def printfun(n):
    """
    :param n: Recebe um numero inteiro.
    :return: Retorna em uma unica linha os valores de 1 até n.
    """
    [print(x, end='') for x in range(1, n + 1)]  # end por padrão é \n, referindo como vazio, temos print em linha unica


printfun(int(input()))
