import subprocess
import os
import datetime
from pathlib import Path
import pytest
import math

# Для Windows
INTERPRETER = 'python'

test_data = {
    'fact': [
        (5, 120),
        (0, 1),
        (1, 1),
        (10**5+1, 'N out of the range'),
        (-2, 'N out of the range')
    ],
    'show_employee': [
        ('Иванов Иван Иванович', '30000', 'Иванов Иван Иванович: 30000 ₽'),
        ('Игорёк', '', 'Игорёк: 100000 ₽'),
        ('  Абдула Рамзес   ', '  78000 ', 'Абдула Рамзес: 78000 ₽'),
        ("", '30000', ': 30000 ₽')
    ],
    'sum_and_sub':[
        (4, 5, (9, -1)),
        (8, 3, (11, 5)),
        (-2.0, 5, (3.0, -7.0)),
        (-5, -6, (-11, 1)),
    ],
    'process_list':[
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 4, 27, 16, 125, 36, 343, 64]),
        ([10, 20, 30, 40], [100, 400, 900, 1600]),
        ([], 'length of the Array is out of range'),
        ([0] * (10**3+1), 'length of the Array is out of range')
    ],
    'my_sum':[
        ([1, 1, 1, 1, 1], 5),
        ([-1, -1, -1, -1], -4),
        ([0, 0], 0),
        ([], 0),
        ([540, -40, 260.0, -60, 100, -100, 0, 5,], 705.0),
    ],
    'my_sum_argv':[
        (['1', '2', '3'], 6),
        (['1.5', '2.5', '3'], 7.0),
        (['-5', '0', '5'], 0),
        ([], 0),
        (['abc', '123', 'jojo', '0.1'], 123.1)
    ],
    'file_sort':[
        ('C:\\Users\\alina\\Downloads\\hw2\\for_test', ['aaa.txt', 'ccc.txt', 'bbb.xlsx']),
    ],
    'file_search':[
        ('ccc.txt', ['first', 'second', 'third', 'fourth', 'fifth']),
        ('notFile.txt', "Файл 'notFile.txt' не найден")
    ],
    'email_validation':[
        ('Haha', False),
        ('Ha@Ha@Ha', False),
        ('H.a@Ha.Ha', False),
        ('@gmail.com', False),
        ('normal@.com', False),
        ('normal@gamil.', False),
        ('normal@gamil.comO', False),
        ('normal@gamil.ru2', False),
        ('!%&?!!!@gamil1.com', False),
        ('lara@mospolytech2.ru', True),
        ('brian-23@mospolytech.ru', True),
        ('britts_54@mospolytech.ru', True),
    ],
    'fibonacci':[
        (5, [0, 1, 1, 2, 3]),
        (2, [0, 1]),
        (1, [0]),
        (15, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]),
        (16, 'N is out if the range [1, 15]'),
        (0, 'N is out if the range [1, 15]'),
        (-1, 'N is out if the range [1, 15]'),
    ],
    'average_scores':[
        ([(80, 90, 78, 93, 80), (90, 91, 85, 88, 86), (91, 92, 83, 89, 90.5)],
        [87.0, 91.0, 82.0, 90.0, 85.5]),
        ([], 'X is out of range (0, 100]'),
        ([()] * 101, 'X is out of range (0, 100]'),  
        ([()], 'N is out of range (0, 100]'),
        ([(0, 1) * 51], 'N is out of range (0, 100]'),
    ],
    'plane_angle':[
        ((0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), 0.0),
        ((0,0,0), (1,0,0), (0,1,0), (1,0,1), 90.0),
        ((0,0,0), (1,0,0), (0,1,0), (2, 2, 1), 25.24),
    ],
    'phone_number':[
        (['07895462130', '89875641230', '9195969878'], ['+7 (789) 546-21-30', '+7 (919) 596-98-78', '+7 (987) 564-12-30']),
        (['01111111111', '3333333333', '+70000000000'], ['+7 (000) 000-00-00', '+7 (111) 111-11-11', '+7 (333) 333-33-33'])
    ],
    'people_sort':[
        ([['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F']], 
     ['Mr. Mike Thomson', 'Ms. Andria Bustle', 'Mr. Robert Bustle']),
        ([['John', 'Smith', '25', 'M'], ['Jane', 'Doe', '25', 'F'], ['Bob', 'Wilson', '25', 'M']], 
     ['Mr. John Smith', 'Ms. Jane Doe', 'Mr. Bob Wilson']),
        ([['P1', '1', '2', 'M'], ['P2', '2', '10', 'M'], ['P3', '3', '1', 'M'], ['P4', '4', '100', 'M']], 
     ['Mr. P3 3', 'Mr. P1 1', 'Mr. P2 2', 'Mr. P4 4']),
        ([['Alice', 'Green', '-5', 'F'], ['Bob', 'Brown', '10', 'M']],
     ['Математическая ошибка']), 
    ],
    'complex_numbers':[
        ((2.0, 1.0), (5.0, 6.0), 
     ['7.00+7.00i', '-3.00-5.00i', '4.00+17.00i', '0.26-0.11i', '2.24+0.00i', '7.81+0.00i']),
        ((0.0, 0.0), (1.0, 1.0),
     ['1.00+1.00i', '-1.00-1.00i', '0.00+0.00i', '0.00+0.00i', '0.00+0.00i', '1.41+0.00i']),
        ((-2.0, -3.0), (1.0, 4.0),
     ['-1.00+1.00i', '-3.00-7.00i', '10.00-11.00i', '-0.82+0.29i', '3.61+0.00i', '4.12+0.00i']),
    ],
}

from fact import fact_it, fact_rec

@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_it(input_data, expected):
    assert fact_it(input_data) == expected
@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_rec(input_data, expected):
    assert fact_it(input_data) == expected


from show_employee import show_employee

@pytest.mark.parametrize("name_data, salary_data, expected", test_data['show_employee'])
def test_show_employee(name_data, salary_data, expected):
    if salary_data:
        assert show_employee(name_data, salary_data) == expected
    else:
        assert show_employee(name_data) == expected


from sum_and_sub import sum_and_sub

@pytest.mark.parametrize("first_num_data, second_num_data, expected", test_data['sum_and_sub'])
def test_sum_and_sub(first_num_data, second_num_data, expected):
    assert sum_and_sub(first_num_data, second_num_data) == expected


from process_list import process_list, process_list_gen

@pytest.mark.parametrize("array_data, expected", test_data['process_list'])
def test_process_list(array_data, expected):
    assert process_list(array_data) == expected
@pytest.mark.parametrize("array_data, expected", test_data['process_list'])
def test_process_list_gen(array_data, expected):
    assert process_list_gen(array_data) == expected


from my_sum import my_sum

@pytest.mark.parametrize("array_data, expected", test_data['my_sum'])
def test_my_sum(array_data, expected):
    assert my_sum(array_data) == expected


from my_sum_argv import my_sum_argv, parse_args

@pytest.mark.parametrize("args, expected", test_data['my_sum_argv'])
def test_full(args, expected):
    assert my_sum_argv(parse_args(args)) == expected


from file_sort import file_sort

@pytest.mark.parametrize("arg, expected", test_data['file_sort'])
def test_file_sort(arg, expected):
    assert file_sort(arg) == expected


from file_search import find_file_os_walk

@pytest.mark.parametrize("arg, expected", test_data['file_search'])
def test_file_search(arg, expected):
    assert find_file_os_walk(arg) == expected


from email_validation import fun

@pytest.mark.parametrize("arg, expected", test_data['email_validation'])
def test_fun(arg, expected):
    assert fun(arg) == expected


from fibonacci import fibonacci

@pytest.mark.parametrize("arg, expected", test_data['fibonacci'])
def test_fibonacci(arg, expected):
    assert fibonacci(arg) == expected


from average_scores import compute_average_scores

@pytest.mark.parametrize("arg, expected", test_data['average_scores'])
def test_compute_average_scores(arg, expected):
    assert compute_average_scores(arg) == expected


from plane_angle import plane_angle, Point

@pytest.mark.parametrize("a_coords, b_coords, c_coords, d_coords, expected", test_data['plane_angle'])
def test_plane_angle(a_coords, b_coords, c_coords, d_coords, expected):
    A = Point(*a_coords)
    B = Point(*b_coords)
    C = Point(*c_coords)
    D = Point(*d_coords)
    
    result = plane_angle(A, B, C, D)

    assert result == pytest.approx(expected, rel=1e-4, abs=1e-4)


from phone_number import sort_phone

@pytest.mark.parametrize("arg, expected", test_data['phone_number'])
def test_sort_phone(arg, expected):
    assert sort_phone(arg) == expected


from people_sort import name_format
@pytest.mark.parametrize("arg, expected", test_data['people_sort'])
def test_name_format(arg, expected):
    assert name_format(arg) == expected


from complex_numbers import Complex

@pytest.mark.parametrize("x, y, expected", test_data['complex_numbers'])
def test_Complex(x, y, expected):
    x = Complex(*x)
    y = Complex(*y)
    result = [str(x+y), str(x-y), str(x*y), str(x/y), str(x.mod()), str(y.mod())]


    assert result == expected



from freezegun import freeze_time
from log_decorator import function_logger

@pytest.fixture
def cleanup_log_files():
    """Фикстура для очистки тестовых лог-файлов"""
    yield
    # Удаляем тестовые файлы после каждого теста
    for file in Path('.').glob('test_*.log'):
        file.unlink()
    for file in Path('.').glob('logs/test_*.log'):
        file.unlink()

@freeze_time("2024-02-19 16:00:12.670738")
def test_function_logger_basic(cleanup_log_files):
    """Тест базового логирования"""
    log_file = 'test_basic.log'
    
    @function_logger(log_file)
    def greeting_format(name):
        return f'Hello, {name}!'
    
    greeting_format('John')
    
    #файл создан
    assert Path(log_file).exists()
    
    with open(log_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    #структуру лога
    assert 'greeting_format' in content
    assert '2024-02-19 16:00:12.670738' in content
    assert "args: ('John',)" in content
    assert 'return: Hello, John!' in content
    assert '0:00:00' in content

@freeze_time("2024-02-19 10:30:45.123456")
def test_function_logger_no_args(cleanup_log_files):
    """Тест функции без аргументов"""
    log_file = 'test_no_args.log'
    
    @function_logger(log_file)
    def say_hello():
        return 'Hello World!'
    
    say_hello()
    
    with open(log_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert 'say_hello' in content
    assert 'args: ()' in content
    assert 'kwargs: {}' in content
    assert 'return: Hello World!' in content