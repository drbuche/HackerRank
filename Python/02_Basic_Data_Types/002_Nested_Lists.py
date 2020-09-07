# Problem : https://www.hackerrank.com/challenges/nested-list/problem
# Score : 10 points(MAX)

n = int(input())  # Numerod e alunos
alunos = [[input(), float(input())] for _ in range(n)]  # Para cada aluno fazemos um input de nome, nota(float)


def organiza(aluno_nota):
    """
    :param aluno_nota: lista de alunos, nota
    :return: aluno com a segunda menor nota, caso haja mesma nota, retorna aluno em ordem alfabética
    """
    segunda_menor = sorted(set([nota for aluno, nota in aluno_nota]))[1]
    """
    Em segunda_menor temos a seguinte logica, criamos um loop para colocar as notas em uma lista
    Após isso, convertemos a lista em set, para que os valores repetidos possuam apenas 1 elemento
    Então ordenamos a lista do menor para o maior e pegamos o elemento [1], segundo menor valor
    """
    return '\n'.join([aluno for aluno, nota in sorted(aluno_nota) if nota == segunda_menor])
    # Por fim, organizamos a lista de alunos pelo nome.
    # Caso a nota do aluno for igual ao segundo_menor ele é retornado em uma lista
    # que separa seus elementos por \n


print(organiza(alunos))
