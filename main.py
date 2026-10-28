import tkinter as tk
from tkinter import messagebox


def calculate_discount():
    try:
        original_price = float(original_price_entry.get())
        discount = float(discount_entry.get())

        if original_price < 0 or discount < 0:
            raise ValueError("Values must be positive.")
        if discount > 100:
            raise ValueError("Discount cannot exceed 100%.")

        discount_amount = original_price * discount / 100
        final_price = original_price - discount_amount

        result_label.config(
            text=f"Discount Amount: {discount_amount:.2f}\n"
            f"Final Price: {final_price:.2f}"
        )
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Please enter valid numbers.\n{e}")


def reset_fields():
    original_price_entry.delete(0, tk.END)
    discount_entry.delete(0, tk.END)
    result_label.config(text="Enter the values and press Calculate.")
    original_price_entry.focus_set()


root = tk.Tk()
root.title("Discount Calculator")
root.geometry("320x260")
root.resizable(False, False)

tk.Label(root, text="Original Price:", font=("Arial", 11)).pack(pady=(15, 2))
original_price_entry = tk.Entry(root, width=25, font=("Arial", 11))
original_price_entry.pack()

tk.Label(root, text="Discount (%):", font=("Arial", 11)).pack(pady=(10, 2))
discount_entry = tk.Entry(root, width=25, font=("Arial", 11))
discount_entry.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Calculate",
    font=("Arial", 11, "bold"),
    width=10,
    command=calculate_discount,
).pack(side=tk.LEFT, padx=5)

tk.Button(
    button_frame,
    text="Reset",
    font=("Arial", 11),
    width=10,
    command=reset_fields,
).pack(side=tk.LEFT, padx=5)

result_label = tk.Label(
    root,
    text="Enter the values and press Calculate.",
    font=("Arial", 10),
    fg="darkgreen",
    justify="center",
)
result_label.pack()

root.mainloop()
