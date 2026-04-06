# Задача 5: Калькулятор скидки

price = 450      # цена за штуку
count = 8        # количество

total = price * count

if total < 1000:
    discount = 0
elif total <= 5000:
    discount = 5
else:
    discount = 10

discount_sum = total * discount / 100
final = total - discount_sum

print("=== КАЛЬКУЛЯТОР СКИДКИ ===")
print(f"Сумма без скидки: {total} руб.")
print(f"Скидка: {discount}%")
print(f"Сумма скидки: {discount_sum} руб.")
print(f"Итого: {final} руб.")