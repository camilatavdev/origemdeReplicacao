#Código usado para encontrar os vizinhos de um padrão de DNA com uma certa distância de Hamming, indicada por 'd'.

# Função para calcular a distância de Hamming entre duas strings:
def hamming_distance(str1, str2):
    # Calcula a distância de Hamming entre duas strings de comprimento igual
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

# Função para encontrar os vizinhos de um padrão de DNA com uma certa distância de Hamming:
def neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
       
    neighborhood = set()

    # Gera todos os k-mers possíveis do comprimento do padrão
    kmer_set = set()
    kmer_set.add(pattern)
  
    # Para cada posição no padrão, gera todas as substituições possíveis:
    for i in range(len(pattern)):
        symbol = pattern[i] 
        for replacement in ['A', 'C', 'G', 'T']:
            if replacement != symbol: 
                neighbor = pattern[:i] + replacement + pattern[i+1:]
                kmer_set.add(neighbor)

    # Gera vizinhos com distância de Hamming d
    for kmer in kmer_set:
        if hamming_distance(pattern, kmer) <= d:
            neighborhood.add(kmer)

    return list(neighborhood)

# Exemplo de uso:
pattern = "AAAAGCCGAG"
d = 2 #número máximo de nucleotídeos que podem ser diferentes entre o padrão original e os vizinhos gerados
result = neighbors(pattern, d) 

for neighbor in result:
    print(neighbor)