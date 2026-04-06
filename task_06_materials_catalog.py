# Задача 6: Каталог материалов

materials = ["Кирпич", "Цемент", "Песок", "Доски", "Гвозди"]

print("=== КАТАЛОГ МАТЕРИАЛОВ ===")
print(f"Список: {materials}")
print(f"Первый: {materials[0]}")
print(f"Последний: {materials[-1]}")
print(f"Средние: {materials[1:4]}")

# Добавляем
materials.append("Бетон")
materials.append("Арматура")
print(f"После добавления: {materials}")

# Удаляем второй элемент (индекс 1)
del materials[1]
print(f"После удаления: {materials}")
print(f"Длина списка: {len(materials)}")