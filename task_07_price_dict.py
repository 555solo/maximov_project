# Задача 7: Прайс-лист материалов

prices = {
    "Кирпич": 15.50,
    "Цемент": 450.00,
    "Песок": 800.00,
    "Доски": 1200.00,
    "Гвозди": 85.00
}

print("=== ПРАЙС-ЛИСТ ===")
for item, price in prices.items():
    print(f"{item}: {price} руб.")

# Добавляем
prices["Бетон"] = 4200.00
prices["Арматура"] = 48000.00

# Изменяем (+10%)
prices["Цемент"] = prices["Цемент"] * 1.10

# Удаляем
del prices["Гвозди"]

print("\n=== ОБНОВЛЕННЫЙ ПРАЙС-ЛИСТ ===")
for item, price in prices.items():
    print(f"{item}: {price:.2f} руб.")

# Средняя цена
avg = sum(prices.values()) / len(prices)
print(f"\nСредняя цена: {avg:.2f} руб.")