# Problem : https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
# Score : 20 points(MAX)


cube = lambda x: x**3  # lambda para fazer x ao cubo


def fibonacci(numero):
    fibo = [0, 1]
    if numero == 0:
        return []
    elif numero == 1:
        return [0]
    for fibo_atual in range(2, numero):
        fibo.append(fibo[fibo_atual - 2] + fibo[fibo_atual - 1])  # Calcular a Sequência de Fibonacci (penúltimo valor mais último)
    return fibo


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

