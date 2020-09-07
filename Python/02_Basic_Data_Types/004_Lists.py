# Problem : https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Score : 10 points(MAX)

n = int(input())  # Quantos comandos serão realizados
lista = []  # Lista final de numeros

for _ in range(n):  # Repita para cada comando
    texto = input().split()  # Pegue o input que possui comando e argumentos e coloque em uma lista separando por ','
    comando = texto[0]  # O primeiro elemento sempre sera o comando, entao atribua a uma variavel
    argumentos = texto[1:]  # Atribu para variavel argumentos os valores de texto começando no elemento 1 até o final
    if comando != "print":  # Caso o comando nao for print
        comando += "(" + ",".join(argumentos) + ")"  # Comando + ( + argumentos separados por , + )
        eval("lista." + comando)  # eval executa o codigo dentro do () como se estivesse escrevendo no terminal
        # Exemplo eval('lista'.insert(0, 5)
    else:
        print(lista)
