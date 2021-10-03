def score(word):
    minuscula = word.lower()
    count = 0
    for x in minuscula:
        if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
            count = count + 1
        if(x == 'l' or x == 'n' or x == 'r' or x == 's' or x == 't'):
            count = count + 1
        if(x == 'd' or x == 'g'):
            count = count + 2
        if(x == 'b' or x == 'c' or x == 'm' or x == 'p'):
            count = count + 3
        if(x == 'f' or x == 'h' or x == 'v' or x == 'w' or x == 'y'):
            count = count + 4
        if(x == 'k'):
            count = count + 5
        if(x == 'j' or x == 'x'):
            count = count + 8
        if(x == 'q' or x == 'z'):
            count = count + 10
    return count        
            