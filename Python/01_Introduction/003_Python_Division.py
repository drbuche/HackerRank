# Problem : https://www.hackerrank.com/challenges/python-division/problem
# Score : 10 points(MAX)

def division(a, b):
    """
    :param a, b: Recebe 2 numeros.
    :return: Retorna o print do resultado int de 'a' dividido por 'b'
             e do resultado da divisão  de 'a' por 'b', separados por '\n'.
    """
    print((a // b), (a / b), sep='\n')


division(int(input()), int(input()))  # Executa a função tendo como parametro 2 inteiros
