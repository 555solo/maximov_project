# Задача 1: Найдите час суток с максимальным числом поездок в выходные дни
import pandas as pd

df = pd.read_csv("5_train.csv")
df["datetime"] = pd.to_datetime(df["datetime"])

# Фильтр: только выходные
weekend = df[df["workingday"] == 0]

# Извлекаем час
hour = weekend["datetime"].dt.hour

# Группировка по часу, среднее число поездок
hourly_avg = weekend.groupby(hour)["count"].mean()

# Поиск максимального
max_hour = hourly_avg.idxmax()
max_value = hourly_avg.max()

print(f"Час с максимальным числом поездок в выходные дни: {max_hour}:00")
print(f"Среднее число поездок в этот час: {max_value:.1f}")