# Problem : https://www.hackerrank.com/challenges/text-alignment/problem
# Score : 10 points(MAX)


# Esse exercício apresenta um método peculiar do Python, ele alinha textos de acordo com a largura.
# .ljust(largura) -> Alinha para esquerda tendo como parametro a largura.
# .center(largura) -> Alinha para o centro tendo como parametro a largura.
# .rjust(largura) -> Alinha para direita tendo como parametro a largura.


thickness = int(input())
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


