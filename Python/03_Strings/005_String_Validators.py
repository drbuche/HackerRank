# Problem : https://www.hackerrank.com/challenges/string-validators/problem
# Score : 10 points(MAX)

# O método .isalnum() retorna True caso haja apenas caracteres alfabéticos e numéricos na string.
# O método .isalpha() retorna True caso todos os caracteres sejam  caracteres alfabéticos.
# O método .isdigit() retorna True caso todos os caracteres sejam  numéricos alfabéticos.
# O método .islower() retorna True caso todos os caracteres sejam  caracteres alfabéticos minúsculos.
# O método .isupper() retorna True caso todos os caracteres sejam  caracteres alfabéticos maiúsculos.

# Leia a palavra e retorne True caso qualquer letra que ela possua retorne True nos métodos acima.

if __name__ == '__main__':

    s = input()
    [print(any(eval('letra.' + metodo) for letra in s)) for metodo in ('isalnum()', 'isalpha()', 'isdigit()', 'islower()', 'isupper()')]
    # imprima na tela True or False utilizando os métodos da lista em cada letra da palavra digitada
    # Método any retorna True caso algum elemento seja True.

    # [print(list(eval('letra.' + metodo) for letra in s)) for metodo in ('isalnum()', 'isalpha()', 'isdigit()', 'islower()', 'isupper()')]
    # Caso troque o any por list(), notará que as listas que possuem ao menos 1 True foram retornadas como True pelo any()


