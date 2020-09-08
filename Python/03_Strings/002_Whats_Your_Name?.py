# Problem : https://www.hackerrank.com/challenges/whats-your-name/problem
# Score : 10 points(MAX)


def print_full_name(a, b):
    '''
    :param a: recebe o primeiro nome
    :param b: recebe o segundo nome
    :return: retorna a frase com esses nomes
    '''
    print(f"Hello {a} {b}! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)