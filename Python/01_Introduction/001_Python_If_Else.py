# Problem : https://www.hackerrank.com/challenges/py-if-else/problem
# Score : 10 points(MAX)

def wierd(n):
    """
    :param n: Recebe um valor inteiro 'n'
    :return: Retona um print contendo 'Weird' caso o numero seja impar ou esteja entre 6 e 20.
             Caso contrario retorna 'Not Weird'.
    """
    print('Weird' if (n % 2 == 1) or (6 <= n <= 20) else 'Not Weird')


wierd(int(input()))  # Executa a função 'wierd' utilizando como parametro um input inteiro.
