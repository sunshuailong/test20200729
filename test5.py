def fibs(n):
    """this is fibonacci"""
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibs(n-1)+fibs(n-2)
print(fibs(10))