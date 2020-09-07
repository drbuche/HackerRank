# Problem : https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Score : 10 points(MAX)

n = input()  # Numero de valores, desnecessário...
print(hash(tuple(map(int, input().split(' ')))))
# Pegue o input (1 2 3) e use como parametro os espaços para separar (1,2,3), em seguida faça o map
# Transformando cada elemento em um numero inteiro, depois transforme em uma tupla e execute o hash

