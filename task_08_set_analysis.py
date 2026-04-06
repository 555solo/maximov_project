# Задача 8: Анализ материалов поставщиков

s1 = ["Песок", "Цемент", "Арматура", "Доски"]
s2 = ["Цемент", "Гвозди", "Бетон", "Кирпич"]
s3 = ["Кирпич", "Цемент", "Песок", "Доски"]

set1 = set(s1)
set2 = set(s2)
set3 = set(s3)

print("=== АНАЛИЗ МАТЕРИАЛОВ ===")
print(f"Все уникальные: {set1 | set2 | set3}")
print(f"Общие для всех: {set1 & set2 & set3}")
print(f"Только у первого: {set1 - set2 - set3}")

# Ровно у двух
from collections import Counter
all_m = s1 + s2 + s3
c = Counter(all_m)
two = [item for item, count in c.items() if count == 2]
print(f"Ровно у двух: {set(two)}")