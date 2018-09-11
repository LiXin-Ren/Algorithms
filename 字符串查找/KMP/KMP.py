def GetNext(p):
    n = len(p)
    next = [-1] * n
    k = -1
    j = 0

    while(j < n - 1):
        # k初始为next[j-1]
        if k == -1 or p[k] == p[j]:
            k += 1
            j += 1
            next[j] = k
        else:
            k = next[k]
    return next

# 改进的next获取方式
def GetNextval(p):
    n = len(p)
    next = [-1] * n

    k = -1
    j = 0

    while j < n-1:
        if k == -1 or p[j] == p[k]:
            k += 1
            j += 1
            #//p[k]表示前缀，p[j]表示后缀
            if p[j] != p[k]:
                next[j] = k
            else:
                # 因为不能出现p[j] = p[next[j]]，所以当出现时需要继续递归，k = next[k] = next[next[k]]
                next[j] = next[k]
        else:
            k = next[k]
    return next



def KmpSearch(s, p):
    next = GetNextval(p)
    sLength = len(s)
    pLength = len(p)
    i = 0
    j = 0

    while(i < sLength and j < pLength):
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == pLength:
        return i - j
    else:
        return -1


s = 'BBC ABCDAB ABCDABCDABDE'
p = 'ABCDABC'
print("next = ", GetNext(p))
print("nextVal = ", GetNextval(p))
print("result = ",KmpSearch(s, p))