def sum_and_sub(a, b):
    return (a + b, a - b)

if __name__ == '__main__':
    print(4, 5, sum_and_sub(4, 5))
    print(8, 3, sum_and_sub(8, 3))
    print(-2.0, 5, sum_and_sub(-2.0, 5))
    print(-5, -6, sum_and_sub(-5, -6))
