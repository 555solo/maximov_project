# Задача 2: Постройте столбчатую диаграмму: среднее число поездок (casual и registered отдельно) по сезонам
import pandas as pd
import matplotlib.pyplot as plt

# Загружаем данные
df = pd.read_csv("5_train.csv")

# Группируем по сезонам и считаем среднее
season_stats = df.groupby("season").agg({
    "casual": "mean",
    "registered": "mean"
})

# Подписываем сезоны
season_names = {1: "Зима", 2: "Весна", 3: "Лето", 4: "Осень"}
season_stats.index = [season_names[i] for i in season_stats.index]

print("=== СРЕДНЕЕ ЧИСЛО ПОЕЗДОК ПО СЕЗОНАМ ===")
print(season_stats.round(1))
print()

# Строим столбчатую диаграмму
season_stats.plot(kind="bar", figsize=(8, 5), color=["steelblue", "coral"])
plt.xlabel("Сезон")
plt.ylabel("Среднее число поездок за час")
plt.title("Среднее число поездок по сезонам")
plt.legend(["Casual (незарегистрированные)", "Registered (зарегистрированные)"])
plt.xticks(rotation=0)
plt.show()