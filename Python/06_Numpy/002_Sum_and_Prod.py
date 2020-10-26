# Problem : https://www.hackerrank.com/challenges/np-sum-and-prod/problem
# Score : 20 points(MAX)


import numpy
n, m = map(int, input().split())  # Atribuir os 2 primeiros valores a variável n e m
matriz = numpy.array([input().split() for _ in range(n)], int)  # Separa os valores inputados de acordo com o tamanho recebido na primeira linha
print(numpy.prod(numpy.sum(matriz, axis=0)))  # Soma o axis de cada coluna da matriz (axis 0 = coluna axis 1 = linha) e depois multiplica o resultado