def proteins(strand):
    protein = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    }
    resultado = []
    num = int(len(strand) / 3)
    for x in range(num):
        condons = strand[x * 3:x * 3 + 3]
        if(protein[condons] == 'STOP'):
            return resultado
        else:
            resultado.append(protein[condons])
    return resultado
