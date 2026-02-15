import sys

def my_sum_argv(numbers):
    if not numbers:
        return 0
    return sum(numbers)

def parse_args(args):
    numbers = []
    for arg in args:
        try:
            numbers.append(int(arg))
        except ValueError:
            try:
                numbers.append(float(arg))
            except ValueError:
                print(f"Предупреждение: '{arg}' не является числом и будет проигнорировано")
    return numbers

def main():
    print(my_sum_argv(parse_args(sys.argv[1:])))

if __name__ == '__main__':
    main()