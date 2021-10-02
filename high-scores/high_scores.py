def latest(scores):
    posicion = len(scores)
    return scores[posicion-1]


def personal_best(scores):
    scores.sort(reverse=True)
    return scores[0]


def personal_top_three(scores):
    scores.sort(reverse=True)
    resultado = scores[:3]
    return resultado
