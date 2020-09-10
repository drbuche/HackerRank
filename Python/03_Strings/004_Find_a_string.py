# Problem : https://www.hackerrank.com/challenges/find-a-string/problem
# Score : 10 points(MAX)

def count_substring(string, sub_string):
    '''
    :param string: Uma palavra
    :param sub_string: Um grupo de letras
    :return: Quantas vezes esse grupo de letras se repete dentro da palavra
    '''
    return sum([1 for x in range(len(string)-len(sub_string)+1) if string[x:x+len(sub_string)] == sub_string])
    #                       O número de letras em 'string' menos o numero de letras em 'sub_string' nos retorna quantas
    # vezes a sub_string pode caminhar pela string, como se estivesse varrendo a palavra
    # Pegue o número atual do loop e atribua a string[n_atual(letra inicial):n_atual + tamanho sub_string(numero final)
    # Então ele ira comparar esse trecho da string com a palavra inteira da sub_string
    # Caso forem iguais, o grupo recebe um elemento 1, exemplo: [1, 1, 1, 1] <- a sub_string ocorreu 4x na string
    # Por fim faça, some e retorne o valor.

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
