#A distância de Hamming é uma maneira de medir o quão diferentes duas palavras são, contando o número de letras que 
#são diferentes entre elas, quando as palavras têm o mesmo tamanho.

def hamming_distance(s1, s2):
    cont_diferencas = 0 

    if len(s1) != len(s2):
        raise ValueError("As strings devem ter o mesmo tamanho")

    for i in range(len(s1)): 
        if s1[i] != s2[i]:
           cont_diferencas += 1

    return cont_diferencas

# Exemplo de uso:

s1 = "CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG"
s2 = "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"
result = hamming_distance(s1, s2)
print(result)