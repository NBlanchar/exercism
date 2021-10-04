def find_anagrams(word, candidates):
    resultado = []
    item_A = sorted(word.upper())
    for anagrama in candidates:
        if word.upper() != anagrama.upper():
            item_B = sorted(anagrama.upper())
            if (item_A == item_B):
                resultado.append(anagrama)
    return resultado
