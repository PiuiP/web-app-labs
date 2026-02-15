import time 

def process_list(arr):
    if (len(arr) < 1 or len(arr) > 10**3):
        return 'length of the Array is out of range'
    result = []
    for i in arr:
        if i % 2 == 0:
            result.append(i**2)
        else:
            result.append(i**3)
    return result

def process_list_gen(arr):
    if (len(arr) < 1 or len(arr) > 10**3):
        return 'length of the Array is out of range'
    return [i**2 if i % 2 == 0 else i**3 for i in arr]

def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    print(process_list(array))

    start = time.perf_counter()
    result_ordinary = process_list(array)
    time_ordinary = time.perf_counter() - start

    start = time.perf_counter()
    result_comprehension = process_list_gen(array)
    time_comprehension = time.perf_counter() - start
    print(f"\nВремя выполнения:")
    print(f"стандартно: {time_ordinary:.8f} сек")
    print(f"list comprehension: {time_comprehension:.8f} сек")

# for len(array) = 8
# Стандартно: 0.00000620 сек
# list comprehension: 0.00000450 сек

if __name__ == '__main__':
    main()
