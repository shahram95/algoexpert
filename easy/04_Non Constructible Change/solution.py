def nonConstructibleChange(coins):
    totalChange = 0
    coins.sort()

    for coin in coins:
        if coin > totalChange+1:
            break
        totalChange += coin
    return totalChange+1