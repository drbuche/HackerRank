# Problem : https://www.hackerrank.com/challenges/text-wrap/problem
# Score : 10 points(MAX)


def wrap(palavra, tamanho_do_grupo):
    '''
    :param palavra: recebemos a palavra que sera quebrada
    :param tamanho_do_grupo: o numero de caracteres em cada grupo
    '''
    return "\n".join([palavra[i:i + tamanho_do_grupo] for i in range(0, len(palavra), tamanho_do_grupo)])
    # Dentro da comprehensions temos um loop que é feito com range de 0(primeira letra) até
    # a ultima letra da palavra(len) pulando a quantia igual ao 'tamanho_do_grupo'
    # O valor atual da range é atribuído a variável 'i'
    # Para cada loop 'for', retornamos a 'palavra' usando como parâmetro de fatiamento a variável 'i',
    # criando uma lista com as palavras separadas de forma ideal
    # Por fim, o exercício pede que cada grupo ocupe 1 única linha, então
    # utilizamos o método " ".join e damos como parâmetro o valor '\n', isso fará com que ele
    # troque o separador ',' por '\n', realizando assim a quebra de linha


if __name__ == '__main__':
    print(wrap(input(), int(input())))