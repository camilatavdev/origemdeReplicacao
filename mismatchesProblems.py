#Encontrar palavras frequentes com discrepância

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

#A função acima (hamming_distance) calcula a distância de Hamming entre duas strings s1 e s2, ou seja, o número de posições em que os símbolos
#correspondentes são diferentes entre as duas strings.

def approximate_pattern_count(text, pattern, d):
    count = 0
    k = len(pattern)

    for i in range(len(text) - k + 1): 
        pattern_prime = text[i:i+k] 
        if hamming_distance(pattern, pattern_prime) <= d:
            count += 1 
    return count

def frequent_words_with_mismatches(text, k, d):
    patterns = set() 
    max_count = 0

    for i in range(len(text) - k + 1): 
        pattern = text[i:i+k] 
        count = approximate_pattern_count(text, pattern, d)

        if count > max_count: 
            max_count = count 
            patterns = {pattern}
        elif count == max_count:
            patterns.add(pattern)

    return list(patterns)

# Exemplo de uso:
text = "TAACGGGGGGACTACTGAGGGGCGTTAACACTACTTAACGGGGGGGAGTAACCGTTAACGGGTAACACTGGGGAGGAGGAGGAGTAACCGTACTACTACTCGTGGGACTTAACGGGACTCGTGGGGGGGAGCGTTAACGGGTAACTAACACTTAACCGTCGTTAACGAGACTGGGACTCGTACTACTGGGCGTGAGTAACACTACTTAACACTTAACGGGGGGTAACCGTCGTGGGGAGGAGGAGGAGACTACTTAACACTCGTTAACGGGGGGGAGGAGACTACTGGGTAACGGGCGTGGGGGGACTGAGTAACCGTGAGGAG"
k = 6
d = 3

result = frequent_words_with_mismatches(text, k, d)
print(result)
