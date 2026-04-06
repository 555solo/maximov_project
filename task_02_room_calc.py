# Задача 2: Параметры помещения
# ===== ИСХОДНЫЕ ДАННЫЕ =====
# Размеры помещения
length = 18.5   # длина помещения в метрах
width = 12.0    # ширина помещения в метрах
height = 3.2    # высота помещения в метрах
price_per_sqm = 125  # стоимость покраски 1 м² (руб.)

# ===== РАСЧЕТЫ =====
# Площадь пола
floor_area = length * width

# Площадь стен (периметр * высота)
# Периметр = 2 * (длина + ширина)
wall_area = 2 * (length + width) * height

# Объем помещения
volume = length * width * height

# Стоимость покраски стен
painting_cost = wall_area * price_per_sqm

# ===== ВЫВОД РЕЗУЛЬТАТОВ =====
print("=" * 50)
print("РАСЧЕТ ПАРАМЕТРОВ ПОМЕЩЕНИЯ")
print("=" * 50)
print(f"Исходные размеры:")
print(f"  Длина: {length} м")
print(f"  Ширина: {width} м")
print(f"  Высота: {height} м")
print()
print(f"Результаты расчетов:")
print(f"  Площадь пола: {floor_area:.2f} м²")
print(f"  Площадь стен: {wall_area:.2f} м²")
print(f"  Объем помещения: {volume:.2f} м³")
print(f"  Стоимость покраски стен: {painting_cost:.2f} руб.")
print("=" * 50)