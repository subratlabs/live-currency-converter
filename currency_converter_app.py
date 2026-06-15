import requests
import tkinter as tk
from tkinter import ttk, messagebox

# window

root = tk.Tk()
root.title("live currency converter")
root.geometry("500x400")
root.config(bg="#1e1e1e")

# title

title = tk.Label(
    root,
    text = "Live Currency Conveter",
    font = ("Arial", 20, "bold"),
    bg = "#1e1e1e",
    fg = "white"
)
title.pack(pady=20)

# currencies

currencies = [
    "USD", "INR", "EUR", "GBP", "JPY", 
    "AUD", "CAD", "CNY", "SGD", "AED"
]

# AMOUNT

amount_label = tk.Label(
    root, 
    text = "Enter Amount",
    font = ("Arial", 12),
    bg = "#1e1e1e",
    fg = "white"
)

amount_label.pack()

amount_entry = tk.Entry(
    root,
    font = ("Arial", 14),
    width = 20
)

amount_entry.pack(pady=10)

# from Currency 

from_label = tk.Label(
    root,
    text="From Currency",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)

from_label.pack()

from_currency = ttk.Combobox(
    root,
    values=currencies,
    font=("Arial", 12),
    state="randonly"
)

from_currency.pack(pady=10)
from_currency.set("USD")

# TO CURRENCY

to_label = tk.Label(
    root,
    text="To Currency",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)

to_label.pack()

to_currency = ttk.Combobox(
    root,
    values=currencies,
    font=("Arial", 12),
    state="randonly"
)

to_currency.pack(pady=10)
to_currency.set("INR")

# result rabel

result_label = tk.Label(
    root,
    text="Converted Amount Will Appear Here",
    font=("arial", 14, "bold"),
    bg="#1e1e1e",
    fg="lightgreen"
)

result_label.pack(pady=20)

# convert function

def convert_currency():
    amount = amount_entry.get()
    from_curr = from_currency.get()
    to_curr = to_currency.get()

    if amount == "":
        messagebox.showerror("Error", "Please enter amount")
        return
    
    try:
        amount = float(amount)

        url = f"https://api.exchangerate-api.com/v4/latest/{from_curr}"
        response = requests.get(url)
        data = response.json()

        rate = data["rates"][to_curr]
        converted_amount = amount * rate

        result_label.config(
            text=f"{amount} {from_curr} = {converted_amount:.2f} {to_curr}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

        # BUTTON 

convert_button = tk.Button(
    root,
    text="Convert",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    padx=20,
    pady=10,
    command=convert_currency
)           

convert_button.pack(pady=20)

root.mainloop()