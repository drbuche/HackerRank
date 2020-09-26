# Problem : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# Score : 10 points(MAX)

def average(arr):
    return (sum(set(arr))) / (len(set(arr)))  # apenas divida a soma de um set pelo seu número de elementos

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
