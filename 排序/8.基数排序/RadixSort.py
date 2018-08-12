import math

def RadixSort(alist, radix = 10):
    if max(alist) == 0:
        K = 1
    else:
        K = int(math.ceil(math.log(max(alist), radix)))      #位数
    for i in range(0, K):
        bucket = [[] for i in range(radix)] #建立radix个桶
        for val in alist:
            bucket[val % (radix**(i+1)) // (radix**i)].append(val) #获得val的第i位数字，并将val放到对应的痛
        del alist[:]
        for each in bucket:
            alist.extend(each)          #合并桶

    return alist

print(RadixSort([321,109 ,584,123, 52, 63,765,814]))