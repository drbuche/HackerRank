# Problem : https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
# Score : 10 points(MAX)

a, b, c, d = (int(input()) for _ in range(4))  # receba 4 números e atribua as variáveis a, b, c, d

print(pow(a, b)+pow(c, d))  # O método pow (recebendo 2 atributos) eleva o primeiro atributo pelo segundo
