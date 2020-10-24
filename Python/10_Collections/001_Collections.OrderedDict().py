# Problem : https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Score : 20 points(MAX)

from collections import OrderedDict
dict = OrderedDict()
for _ in range(int(input())):
    i = input().rpartition(" ")
    dict[i[0]] = int(i[-1]) + dict[i[0]] if i[0] in dict else int(i[-1])
for componente in dict:
    print(componente, dict[componente])