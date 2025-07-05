import pandas as pd

df = pd.read_csv("attendance.csv", names=["Name", "Date", "Time"])

df_sorted = df.sort_values(by=["Name", "Date", "Time"])

df_first_per_day = df_sorted.drop_duplicates(subset=["Name", "Date"], keep="first")

print("\nHer kişinin her gün için ilk gelişi:\n")
print(df_first_per_day.to_string(index=False))
