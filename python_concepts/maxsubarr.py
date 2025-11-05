#window sliding technique
def msarr(arr):
    n = len(arr)
    if n < k:
        print("Invalid")
        return -1

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(window_sum, max_sum)
    return max_sum

arr = [5, 2, -1, 0, 3]
k = 3
print(msarr(arr))


#kadane's algorithm
def maxsubarr(arr):
    n = len(arr)
    currSum = 0
    maxSum = -1e8

    for i in range(0, n):
        currSum = currSum + arr[i]
        if currSum > maxSum:
            maxSum = currSum
        elif currSum < 0:
            currSum = 0 
    return maxSum 

print(maxsubarr([20, 5, -10, -16, 7, 6]))

#mininum sum (similar to maximum sum but reversed)
def minsubarr(arr):
    n = len(arr)
    current_sum = 0 
    minSum = 1e9

    for i in range(0, n):
        current_sum = current_sum + arr[i]
        if current_sum < minSum:
            minSum = current_sum 
        elif current_sum > 0:
            current_sum = 0
    return minSum

print(minsubarr([-4, 5, -1, -6, 8, 9]))


