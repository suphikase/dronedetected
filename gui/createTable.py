import tkinter as tk
import tkinter.ttk as ttk
from update.wifiTab import columns

def create_table(parent, data):
    global tree
    tree = ttk.Treeview(parent, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="w")

    for row in data:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill=tk.BOTH)