# Задача 4: Сохраните в CSV таблицу: средняя температура и среднее число поездок по каждому месяцу
import pandas as pd

# Загружаем данные
df = pd.read_csv("5_train.csv")
df["datetime"] = pd.to_datetime(df["datetime"])

# Извлекаем месяц
df["month"] = df["datetime"].dt.month

# Группировка по месяцу: средняя температура и среднее число поездок
monthly_stats = df.groupby("month").agg({
    "temp": "mean",
    "count": "mean"
}).round(2)

# Сохраняем в CSV
monthly_stats.to_csv("monthly_stats.csv", sep=";")

print("Файл monthly_stats.csv сохранен")