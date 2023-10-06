import time

def divisor(N):
    divi = 0
    sqrtn = int(N ** 0.5)
    for i in range(1, sqrtn+ 1):
        if N % i == 0:
            divi += 2
    if sqrtn * sqrtn == N:
            divi -= 1
    return divi
N = int(input())
start = time.time()
print(divisor(N))
end = time.time()
print(f'solve() elapsed time( : {end - start})')