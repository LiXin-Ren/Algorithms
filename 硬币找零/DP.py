#可以使用动态规划来解决

# 动态编程解决方案将找从零一分钱开始，并系统地找到我们需要的找零额。
# 保证我们在算法的每一步，已经知道为更小的数量进行找零所需要的最小硬币数量

def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] < coinCount:
                coinCount = minCoins[cents-j] + 1
        minCoins[cents] = coinCount

    return minCoins[change]

#print(dpMakeChange([1, 5, 10, 25], 63, [0]*64))


#改进：跟踪找零的硬币，不仅得到最小数目也返回找零列表

def dpMakeChange(coinValueList, change, minCoins, coinUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1

        for j in [c for c in coinValueList if c <= cents]:
            if coinCount > minCoins[cents - j] + 1:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin -= thisCoin


def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinsUsed = [0]*(amnt + 1)
    coinCount = [0]*(amnt + 1)

    print("Making change for", amnt, "requires")
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins")
    print("They are:")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()
#[1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 10, 1, 1, 1, 1, 5, 1, 1, 1, 1, 10, 21, 1, 1, 1, 25, 1, 1, 1, 1, 5, 10, 1, 1, 1, 10, 1, 1, 1, 1, 5, 10, 21, 1, 1, 10, 21, 1, 1, 1, 25, 1, 10, 1, 1, 5, 10, 1, 1, 1, 10, 1, 10, 21]