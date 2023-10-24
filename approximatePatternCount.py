#Implementação da contagem de padrões aproximados

#calcula o número de ocorrências de um determinado padrão em uma determinada string de texto, permitindo um número máximo de discrepâncias,
#ou "mismatches", entre o padrão e a subsequência de texto

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2)) #retorne a soma de quando c1 for diferente de c2 dentro do zip de s1 e s2

#na função acima:
  #s1: É uma das strings de entrada que está sendo comparada para calcular a distância de Hamming.
  #s2: É a outra string de entrada que está sendo comparada com s1.
  #c1: Representa um caractere específico na string s1 durante a iteração.
  #c2: Representa o caractere correspondente na mesma posição em s2 durante a iteração.

def count_with_mismatches(text, pattern, d):
    k = len(pattern)
    count = 0

    for i in range(len(text) - k + 1): 
        substring = text[i:i+k]
        if hamming_distance(pattern, substring) <= d:
            count += 1 

    return count

# Sample Input
text = "CATGCCATTCGCATTGTCCCAGTGA"
pattern = "CCC"
d = 2

# Compute and print the count with at most 2 mismatches
result = count_with_mismatches(text, pattern, d)
print(result)