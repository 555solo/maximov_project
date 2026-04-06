# Задача 10: Система учёта склада

warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}

print("=== СИСТЕМА УЧЁТА СКЛАДА ===")
print(f"{'Материал':<12} {'Кол-во':<8} {'Цена':<10} {'Мин':<8} {'Стоимость':<12}")
print("-" * 55)

total = 0
critical = []
most_expensive = ("", 0)

for name, data in warehouse.items():
    cost = data["quantity"] * data["price"]
    total += cost

    if data["quantity"] < data["min_quantity"]:
        critical.append(name)

    if cost > most_expensive[1]:
        most_expensive = (name, cost)

    print(f"{name:<12} {data['quantity']:<8} {data['price']:<10.2f} {data['min_quantity']:<8} {cost:<12.2f}")

print("-" * 55)
print(f"ОБЩАЯ СТОИМОСТЬ: {total:.2f} руб.")
print(f"Самый дорогой: {most_expensive[0]} ({most_expensive[1]:.2f} руб.)")
print(f"Критические остатки: {critical}")

# Выдача материала
print("\n=== ВЫДАЧА МАТЕРИАЛА ===")
item = "Цемент"
amount = 25
if warehouse[item]["quantity"] >= amount:
    warehouse[item]["quantity"] -= amount
    print(f"Выдано {amount} ед. '{item}'")
    print(f"Остаток: {warehouse[item]['quantity']}")
else:
    print(f"Недостаточно '{item}' на складе")