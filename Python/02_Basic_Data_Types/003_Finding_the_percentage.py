# Problem : https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Score : 10 points(MAX)

n = int(input())  # Numero de Alunos
lista_estudantes = {}  # Dict de aluno, notas

for _ in range(n):  # Repita para cada aluno
    nome, *notas = input().split()  # input o valor nome e *varias(args) notas e separa todos com slip(,)
    nota = list(map(float, notas))  # Pege as notas e converta str para float em cada uma(map), e aloque em uma lista
    lista_estudantes[nome] = nota  # Coloque esse valor na lista_estudante, chave[nome] = valor nota {nome>nota}
qual_nome = input()  # Receba um nome


def soma(nome_busca):
    """
    :param nome_busca: Nome para busca
    :return: média de notas com 2 casas decimais após a virgula do nome_busca
    """
    return '{:.2f}'.format(sum(lista_estudantes[nome_busca]) / 3)
    # Dentro da lista_estutante, selecione a key nome_busca, some as notas, divida por 3 e por fim formate para 2 casas


print(soma(qual_nome))
