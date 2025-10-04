import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())

        if principal < 0 or time < 0 or rate < 0:
            messagebox.showerror("Input Error", "Please enter non-negative values for all inputs.")
            return
        simple_interest = (principal * time * rate) / 100
        compound_interest = principal * ((1 + rate / 100)**time) - principal

        simple_interest_result_label.config(text=f"Simple Interest: {simple_interest:.2f}")
        compound_interest_result_label.config(text=f"Compound Interest: {compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for principal, time, and rate.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
app = tk.Tk()
app.title("Interest Calculator")

tk.Label(app, text="Principal Amount:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
principal_entry = tk.Entry(app)
principal_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Time Period (years):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
time_entry = tk.Entry(app)
time_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="Rate of Interest (%):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
rate_entry = tk.Entry(app)
rate_entry.grid(row=2, column=1, padx=10, pady=5)

calculate_button = tk.Button(app, text="Calculate Interest", command=calculate_interest)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

simple_interest_result_label = tk.Label(app, text="Simple Interest: ")
simple_interest_result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

compound_interest_result_label = tk.Label(app, text="Compound Interest: ")
compound_interest_result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="w")

app.mainloop()
