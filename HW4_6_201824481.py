def isAlpha(L):
    if len(L) <= 1:
        return True
    elif L[0] > L[1]:
        return False
    else:
        return isAlpha(L[1:])
