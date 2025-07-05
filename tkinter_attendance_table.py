import pandas as pd
import tkinter as tk
from tkinter import ttk

df = pd.read_csv("attendance.csv", names=["Name", "Date", "Time"])
df_sorted = df.sort_values(by=["Name", "Date", "Time"])
df_first_per_day = df_sorted.drop_duplicates(subset=["Name", "Date"], keep="first")

root = tk.Tk()
root.title("Günlük İlk Yoklama Tablosu")
root.geometry("600x450")

search_var = tk.StringVar()

def update_table(*args):
    search_term = search_var.get().lower()
    for row in tree.get_children():
        tree.delete(row)

    for _, row in df_first_per_day.iterrows():
        if (
            search_term in str(row["Name"]).lower()
            or search_term in str(row["Date"]).lower()
            or search_term in str(row["Time"]).lower()
        ):
            tree.insert("", "end", values=(row["Name"], row["Date"], row["Time"]))

search_var.trace_add("write", update_table)

search_frame = tk.Frame(root)
search_frame.pack(fill="x", padx=10, pady=5)

tk.Label(search_frame, text="🔍 Ara:").pack(side="left")
tk.Entry(search_frame, textvariable=search_var, width=30).pack(side="left", padx=5)

tree = ttk.Treeview(root, columns=("Name", "Date", "Time"), show="headings")
tree.heading("Name", text="İsim")
tree.heading("Date", text="Tarih")
tree.heading("Time", text="Saat")
tree.column("Name", width=180)
tree.column("Date", width=100)
tree.column("Time", width=100)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tree.pack(expand=True, fill="both", padx=10, pady=(0, 10))

update_table()

root.mainloop()
