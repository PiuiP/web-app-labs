import random
import math

def circle_square_mk(r, n):
    # kвадрат со стороной 2r, в который вписан круг
    # pлощадь квадрата = (2r)^2 = 4r^2
    points_inside = 0
    
    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        
        if x**2 + y**2 <= r**2:
            points_inside += 1
    
    square_area = (2 * r) ** 2
    circle_area = (points_inside / n) * square_area
    
    return circle_area

if __name__ == '__main__':
    r = float(input("Введите радиус: "))
    n = int(input("Введите количество экспериментов: "))
    
    mk_area = circle_square_mk(r, n)
    real_area = math.pi * r ** 2
    error = abs(mk_area - real_area)
    
    print(f"Площадь методом Монте-Карло: {mk_area:.6f}")
    print(f"Точная площадь: {real_area:.6f}")
    print(f"Абсолютная погрешность: {error:.6f}")
    print(f"Относительная погрешность: {error/real_area*100:.4f}%")

"""
ОЦЕНКА ПОГРЕШНОСТИ:

При n = 100:      погрешность ~ 10
При n = 1 000:    погрешность ~ 3-5%
При n = 10 000:   погрешность ~ 1-2%

"""