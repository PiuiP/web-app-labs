import os
import sys

def file_sort(directory):
    try:
        items = os.listdir(directory) #list of dir in directory

        files = []
        for item in items:
            full_path = os.path.join(directory, item)
            if os.path.isfile(full_path):
                files.append(item)
        
        # Сортируем файлы:
        # 1. Сначала по расширению (без точки)
        # 2. Затем по имени файла (без расширения)
        files.sort(key=lambda x: (os.path.splitext(x)[1].lower(), 
                                  os.path.splitext(x)[0].lower()))
        
        return files
    
    except FileNotFoundError:
        print(f"Ошибка: директория '{directory}' не найдена", file=sys.stderr)
        return []
    except PermissionError:
        print(f"Ошибка: нет доступа к директории '{directory}'", file=sys.stderr)
        return []
    except NotADirectoryError:
        print(f"Ошибка: '{directory}' не является директорией", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Неизвестная ошибка: {e}", file=sys.stderr)
        return []

def main():
    if len(sys.argv) != 2:
        print("Использование: python files_sort.py <путь_к_директории>")
        print("Пример: python files_sort.py ./my_folder")
        sys.exit(1)
    
    sorted_files = file_sort(sys.argv[1])
    
    for filename in sorted_files:
        print(filename)

if __name__ == '__main__':
    main()
