import os
import sys

def find_file_os_walk(filename):
    start_dir = os.path.dirname(os.path.abspath(__file__))
    
    for root, dirs, files in os.walk(start_dir):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        
        if filename in files:
            filepath = os.path.join(root, filename)
            print(f"Файл найден: {filepath}")
            print("Первые 5 строк файла:")
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = []
                    for i, line in enumerate(f):
                        if i >= 5:
                            break
                        line = line.rstrip()
                        lines.append(line)
                        print(line)
                    print("-" * 40)
                    return lines
            except Exception as e:
                print(f"Ошибка при чтении файла: {e}")
                return False
    
    return f"Файл '{filename}' не найден"

def main():
    if len(sys.argv) != 2:
        print("Использование: python file_search.py <имя_файла>")
        print("Пример: python file_search.py test.txt")
        sys.exit(1)
    
    filename = sys.argv[1]
    result = find_file_os_walk(filename)
    
    if isinstance(result, str) and "не найден" in result:
        print(result)

if __name__ == '__main__':
    main()