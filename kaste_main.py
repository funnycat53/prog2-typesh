from kaste import kaste
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Kastes īpašības")
root.geometry("400x300")

visas_kastes = []

frame = ttk.Frame(root)
options = {"padx": 5, "pady 5": 5}

# Nosaukums label
Nosaukums_label = ttk.Label(frame, text='Nosaukums')
Nosaukums_label.grid(column=0, row=0, sticky='E', **options)

# Pielietojums label
Pielietojums_label = ttk.Label(frame, text='Pielietojums')
Pielietojums_label.grid(column=0, row=1, sticky='E', **options)

# Izmers label
Izmers_label = ttk.Label(frame, text='Izmers')
Izmers_label.grid(column=0, row=2, sticky='E', **options)
