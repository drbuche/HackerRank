# Problem : https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Score : 20 points(MAX)

from collections import OrderedDict
dict = OrderedDict()  # Instanciando OrderedDict, responsável por reorganizar o dicionário que criaremos
for _ in range(int(input())):
    i = input().rpartition(" ")  # rpartition pesquisa a última ocorrência do que esta entre aspas e divide a a frase em 2 ( objeto, valor)
    dict[i[0]] = int(i[-1]) + dict[i[0]] if i[0] in dict else int(i[-1])  # Armazenando o input no OrderedDict
for valor in dict:
    print(valor, dict[valor])  # retorna o objeto + valor somado