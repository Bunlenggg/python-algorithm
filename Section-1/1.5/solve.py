# Solution 1

# import time
# def prime(N):
#     if N <= 1:
#         return False
#     for i in range(2, N):
#         if N % i == 0:
#             return False
#     return True
# N = int(input())
# start = time.time()
# print("YES" if prime(N) else "NO")
# end = time.time()
# print(f'solve() elapsed time( : {end - start})')

#  Solution 2
import time


def prime(N):
    if N <= 1:
        return False
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True


N = int(input())
start = time.time()
print("YES" if prime(N) else "NO")
end = time.time()
print(f'solve() elapsed time( : {end - start})')
