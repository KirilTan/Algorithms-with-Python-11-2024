def longest_upward_trend(prices, k):
    n = len(prices)
    dp = [1] * n  # dp[i] represents the length of the longest trend ending at i
    prev = [-1] * n  # Keeps track of previous index in the trend

    # Find the longest trend for each price
    for i in range(1, n):
        for j in range(i):
            if prices[i] > prices[j] and abs(prices[i] - prices[j]) <= k:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

    # Find the index of the maximum length trend
    max_length = max(dp)
    max_index = dp.index(max_length)

    # Reconstruct the trend
    trend = []
    while max_index != -1:
        trend.append(prices[max_index])
        max_index = prev[max_index]

    return list(reversed(trend))


# Input reading
prices = list(map(int, input().split(', ')))
k = int(input())

# Find the longest upward trend
result = longest_upward_trend(prices, k)

# Print the result
print(' '.join(map(str, result)))
