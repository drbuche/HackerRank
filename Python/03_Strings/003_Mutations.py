# Problem : https://www.hackerrank.com/challenges/python-mutations/problem
# Score : 10 points(MAX)

def mutate_string(string, position, character):
    '''
    :param string: recebe a palavra
    :param position: refere a posição da letra que deve ser trocada
    :param character: nova letra
    :return:
    '''

    return string[:int(position)]+character+string[int(position)+1:]
    # Recaptulando: [valor1 : valor2 : valor3]-> O primeiro valor aponta o inicio da leitura.
    #                                         -> O segundo refere onde termina - 1 (como em um range).
    #                                         -> O terceiro refere de quanto em quanto ira pular.
    # Estamos falando: na string[::] retorne -> string[de 0 até a posição escolhida] + nova letra + [da posição escollh-
    #                                                                                                ida +1 até o final]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


