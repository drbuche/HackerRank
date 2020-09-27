# Problem : https://www.hackerrank.com/challenges/py-set-add/problem
# Score : 10 points(MAX)


loops = input()  # Quantidade de valores que entrarão
grupo = []  # Grupo para alocar esses valores
[grupo.append(input()) for i in range(int(loops))]  # para cada loop adicione a palavra no grupo dist
print(len(set(grupo)))  # Transforme a lista em um set para remover os valores repetidos e depois retorne o tamanho do set




