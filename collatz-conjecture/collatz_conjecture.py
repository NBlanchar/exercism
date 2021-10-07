def steps(x):
    if(x > 0):
        count = 0
        while(x != 1):
            if(x % 2 == 0):
                x = x/2
            else:
                x = 3*x + 1
            count = count + 1
        return count
    else:
        raise ValueError('error')
