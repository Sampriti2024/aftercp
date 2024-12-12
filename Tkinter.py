import tkinter as tk

def convert_to_cm():
    inches = float(inches_entry.get())
    cm = inches * 2.54
    result_label.config(text=f"{inches} inches is equal to {cm:.2f} centimeters")

root = tk.Tk()
root.title("Inches to Centimeters Converter")

inches_label = tk.Label(root, text="Enter length in inches:")
inches_label.pack()
inches_entry = tk.Entry(root)
inches_entry.pack()

convert_button = tk.Button(root, text="Convert to Centimeters", command=convert_to_cm)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()