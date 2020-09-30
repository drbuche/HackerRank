# Problem : https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# Score : 10 points(MAX)


# os grupos devem estar dentro de um set para aplicarmos o método 'symmetric_difference'
_, a = input(), set(input().split()) # _ recebe o tamanho do set (irrelevante p/ resultado, está ai apenas por exigência do exercício) e 'a' recebe o grupo de numeros
_, b = input(), set(input().split()) # _ recebe o tamanho do set (irrelevante p/ resultado, está ai apenas por exigência do exercício) e 'b' recebe o grupo de numeros
print(len(a.symmetric_difference(b))) # symmetric_difference é um método que retorna os numeros diferentes entre 2 sets, len retorna o tamanho desse grupo de diferenças