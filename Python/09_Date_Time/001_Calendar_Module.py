# Problem : https://www.hackerrank.com/challenges/calendar-module/problem
# Score : 10 points(MAX)

import calendar

m, d, y = map(int, input().split())  # O input deve ser feito: mês, dia e ano, como proposto pelo challange

print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())
# O primeiro argumento 'list', gera uma lista com os dias da semana.
# O segundo método 'calendar.weekday' recebe como parametro 'ano, mês e dia' (nesta ordem) e nos retorna um número que representa o dia da semana.
# Este número selecionará o dia da semana da primeira lista.
# Por fim, retornará o dia da semana em maiúsculo (upper()) como proposto pelo challange
