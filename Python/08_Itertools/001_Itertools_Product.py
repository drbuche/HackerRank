# Problem : https://www.hackerrank.com/challenges/itertools-product/problem
# Score : 10 points(MAX)

from itertools import product

a = map(int, input().split())  # Como receberemos os valores em uma única linha, o split irá separá-los removendo o espaço.
b = map(int, input().split())  # E para cada valor no input, o map transformará em int.

print(*product(a, b))  # O método product cria um laço 'for' realizando todas as uniões possiveis entre os 2 grupos.
                       # ((x,y) for x in A for y in B).
