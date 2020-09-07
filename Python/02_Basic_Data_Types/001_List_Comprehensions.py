# Problem : https://www.hackerrank.com/challenges/list-comprehensions/problem
# Score : 10 points(MAX)

def cubo(x, y, z, n):
    """
    :param x, y, z: valores maximos relacionados a lista [i, j, k]
    :param n: A soma de i, j, k não pode ser igual
    :return: Todas as listas com soma diferente de 'n'
    """
    return [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    #   a lista é composta por -> i valendo de 0 até x, o mesmo se aplica a j, k com seus respectivos relacionais
    #  por fim a lista é acrescentada caso a soma da mesma seja diferente de 'n'


print(cubo((int(input())), (int(input())), (int(input())), (int(input()))))

