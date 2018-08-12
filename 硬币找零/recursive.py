#找出最少数量的找零方式
#用递归实现

#假设有1、5、10、25四种零钱
#numcoins = min((1 + numcoins(originalamout - 1),
# (1 + numcoins(originalamout - 5),
# (1 + numcoins(originalamout - 10),
# (1 + numcoins(originalamout - 25))

#方法一
#这种方式很低效。需要67,716,925次调用
def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1

    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

#print(recMC([1, 5, 10, 25], 63))

#方法二：方法一的改进，将最小数量的硬币结果存储在表中，然后再计算新的最小值之前，先检查表，如果结果已知就直接使用。
#只需221次调用
def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
    elif knownResults[change] > 0:
        return knownResults[change]

    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change-i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

print(recDC([1, 5, 10, 25], 63, [0]*64))
