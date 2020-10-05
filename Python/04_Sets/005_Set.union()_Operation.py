# Problem : https://www.hackerrank.com/challenges/py-set-union/problem
# Score : 10 points(MAX)

_, a = input(), set(input().split()) #recebe o primeiro número (irrelevante) e uma sequência de números que serão colocados em um set, como recebemos os valores em uma única linha, utilizamos o método split(), isso removera um elemento " " dentro do set.
_, b = input(), set(input().split())
print(len(a.union(b)))  # O método union realiza a união ddos grupos e len nos retorna o tamanho do set.

