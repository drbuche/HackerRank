# Problem : https://www.hackerrank.com/challenges/python-mod-divmod/problem
# Score : 10 points(MAX)


a, b = int(input()), int(input())  # receba valor 'a' e 'b'

print(f'{a // b}\n{a % b}\n{divmod(a, b)}')
'''
retorne o resultado inteiro de a/b,
pule uma linha,
retorne o resto de a/b,
pule uma linha,
retorne uma tulpa com o coeficientes e o resto
'''

