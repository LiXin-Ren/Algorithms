# -*- coding:utf-8 -*-
"""
判断是否为旋转词
"""

def nextVal(p, lenp):
    next = [-1] * lenp
    k = -1
    j = 0
    while j < lenp - 1:
        if k == -1 or p[k] == p[j]:
            k += 1
            j += 1
            next[j] = k
        else:
            k = next[k]
    return next

def kmp(s, p, lens, lenp):
    nextList = nextVal(p, lenp)
    i = 0           #长串a的索引
    j = 0
    while (i < lens and j < lenp):
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = nextList[j]
    if j == lenp:
        return True
    return False


def chkRotation(A, lena, B, lenb):
    # write code here
    if lena != lenb:
        return False
    A = A+A
    return kmp(A, B, len(A), lenb)

print(chkRotation("RFSPUYLYR",9,"UYLYRRFSP",9))