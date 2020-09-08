# Problem : https://www.hackerrank.com/challenges/swap-case/problem
# Score : 10 points(MAX)

def swap_case(s):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in s])


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


"""
Imprima na tela ->
para cada letra no input faça ->
se a letra é maiúscula(issupper) 
    ->transforme em minúscula(lower)
se nao
    ->transforme em maiúscula(upper)
    
ao final você tera uma lista com todas as letras ['x', 'y', ' ',...]
pegue essa lista e una seus elementos (.join) trocando o separador (virgula) por um espaço em branco (' '.)
"""

