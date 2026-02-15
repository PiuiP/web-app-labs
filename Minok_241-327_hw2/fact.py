import time

def fact_rec(n):
    if (n < 0 or n > 10**5):
        return 'N out of the range'
    if (n == 1 or n == 0):
        return 1
    return n * fact_rec(n-1)

def fact_it(n):
    if (n < 0 or n > 10**5):
        return 'N out of the range'
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def main():
    n = int(input())
    print(fact_rec(n))

    start = time.perf_counter()
    result_it = fact_it(n)
    time_it = time.perf_counter() - start

    start = time.perf_counter()
    result_rec = fact_rec(n)
    time_rec = time.perf_counter() - start
    print(f"\nВремя выполнения:")
    print(f"Итеративно: {time_it:.8f} сек")
    print(f"Рекурсивно: {time_rec:.8f} сек")

# for n = 5
# Итеративно: 0.00002000 сек
# Рекурсивно: 0.00000190 сек


if __name__ == '__main__':
    main()

