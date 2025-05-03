from colorama import init, Fore, Style

init(autoreset=True)

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    last_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_used[i] = coin

    result = {}
    while amount > 0:
        coin = last_used[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result

# Тест
amount1 = 118
amount2 = 112

print(Fore.GREEN + Style.BRIGHT + f"Greedy algorithm result for {amount1}:")
print(Fore.GREEN + str(find_coins_greedy(amount1)))

print(Fore.CYAN + Style.BRIGHT + f"\nDynamic programming result for {amount2}:")
print(Fore.CYAN + str(find_min_coins(amount2)))
