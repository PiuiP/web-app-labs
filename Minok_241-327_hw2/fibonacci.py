cube = lambda x: x**3

def fibonacci(n):
    if n < 1 or n > 15:
        return 'N is out if the range [1, 15]'
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    res = [0, 1]
    for i in range(2, n):
        res.append(res[i-1] + res[i-2])
    return res

if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
    print(list(map(cube, fibonacci(n))))
