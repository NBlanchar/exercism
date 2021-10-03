def distance(strand_a, strand_b):
    count = 0
    if(len(strand_b) != len(strand_a)):
        raise ValueError('diferentes tamaños')
    num = strand_a
    for x in range(len(num)):
        caracter_a = strand_a[0]
        caracter_b = strand_b[0]
        if(caracter_a != caracter_b):
            count = count + 1
        strand_a = strand_a[1:]
        strand_b = strand_b[1:]
    return count
