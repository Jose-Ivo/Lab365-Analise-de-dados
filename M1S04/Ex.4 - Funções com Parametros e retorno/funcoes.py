
def media(numbers):   #Efetua a soma e depois, tras o resultado da média dividindo o resultado da soma pela quantidade de numeros na lista
    soma = sum(numbers)
    media = soma / len(numbers)
    return media

def maior_menor(numbers): # Retorna o maior e o menor numero
    maior = max(numbers)
    menor = min(numbers)
    return maior, menor

def exibir(numbers): # Exibe as 2 funções com apenas uma chamada
    result1 = media(numbers)
    result2 = maior_menor(numbers)
    print(f"Média: {result1}")
    print(f"Maior numero: {result2[0]}, Menor numero: {result2[1]}")


lista = [10, 20, 30, 40, 50]
exibir(lista)
