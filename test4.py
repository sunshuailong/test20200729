def fibs(n):
    res =[0,1]
    for i in range(n-2):
        res.append(res[-2]+res[-1])
    return res

print(dir(fibs))