# Задача 3: Фильтр: найдите все наблюдения, где count > 500 — сколько их? В какое время года чаще всего?
import pandas as pd

# Загружаем данные
df = pd.read_csv("5_train.csv")

# Фильтр: только наблюдения с count > 500
high_rides = df[df["count"] > 500]

# Сколько таких наблюдений
count_high = len(high_rides)

# Группировка по сезонам
season_counts = high_rides.groupby("season").size()
season_names = {1: "Зима", 2: "Весна", 3: "Лето", 4: "Осень"}
max_season = season_counts.idxmax()

print(f"Количество наблюдений с count > 500: {count_high}")
print(f"Чаще всего в следующее время года: {season_names[max_season]}")