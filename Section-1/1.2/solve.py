# Method 1

# N = int(input())
# sumN = (N * (N + 1)) / 2  # formula for finding sum of natural number
# print(int(sumN))

# # Method 2

# def solve(N):
#     sumN = 0
#     for i in range(1, N + 1):
#         sumN += i
#     return sumN

# N = int(input())
# print(solve(N))

# Another one

def solve(n):
    return n * (n + 1) // 2


n = int(input())
print(solve(n))
