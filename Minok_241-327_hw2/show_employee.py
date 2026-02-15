def show_employee(name, salary='100000'):
    return f'{name.strip()}: {salary.strip()} ₽'

def main():
    name = input().strip()
    salary = input().strip()
       
    if not salary:
        print(show_employee(name)) #В случае, если значение заработной платы /не было передано/ при вызове функции
    else:
        print(show_employee(name, salary))

if __name__ == '__main__':
    main()