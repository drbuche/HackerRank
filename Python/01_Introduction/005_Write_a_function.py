# Problem : https://www.hackerrank.com/challenges/write-a-function/problem
# Score : 10 points(MAX)

def is_leap(year):
    """
    :param year: Recebe um valor referente ao ano.
    :return: Retorna se o ano é bissexto ou não em forma de boolean.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(is_leap(int(input())))
