def maxValue( w, v, n, cap):
    storedp = [-1 for i in range(cap + 1)]
    res = [0 for i in range(n)]

    storedp[0] = 0
    for i in range(n):
        for j in range(cap, w[i] - 1, -1):
            if (storedp[j - w[i]] != -1):
                if storedp[j - w[i]] + v[i] > storedp[j]:
                    res[i] = 1
                    storedp[j] = max(storedp[j - w[i]] + v[i], storedp[j])

    print("res: ", res)
    print("f: ", storedp)
    return max(storedp)

#print(maxValue([1,2,3],[1,2,3],3,6))
print(maxValue([1, 2, 3, 4, 5],[5, 4,3,2, 1], 5, 10))