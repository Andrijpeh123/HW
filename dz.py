import tkinter as tk
from tkinter import ttk
import tkinter.colorchooser
def color():
    rgb_color, web_color = tkinter.colorchooser.askcolor(parent=root, initialcolor=(255, 0, 0))
    color_entry.config(bg=web_color)
def show_results():
    car_type = car_type_var.get()
    age = age_var.get()
    brand = brand_var.get()
    engine = engine_var.get()
    continent = continent_var.get()
    engine_type = engine_type_var.get()
    color = color_entry.cget("bg")
    car_type_text = "Новий автомобіль" if car_type == 1 else "Іноземного виробництва" if car_type == 2 else ""
    age_text = {1: "До 5 років", 2: "6-10 років", 3: "11-15 років", 4: "Більше 15 років"}.get(age, "")
    brand_text = brand if brand != "" else ""
    engine_text = {1: "Менше 1200", 2: "1200-1500", 3: "1501-2200", 4: "Більше 2200"}.get(engine, "")
    continent_text = continent if continent != "" else ""
    engine_type_text = engine_type if engine_type != "" else ""
    color_text = color if color != "" else ""
    result = f"Тип автомобіля: {car_type_text}\n" \
             f"Вік автомобіля: {age_text}\n" \
             f"Марка автомобіля: {brand_text}\n" \
             f"Об'єм двигуна: {engine_text}\n" \
             f"Континент виробника: {continent_text}\n" \
             f"Вид двигуна: {engine_type_text}\n" \
             f"Колір: {color_text}"
    result_label.config(text=result)
def clear_selection():
    car_type_var.set(0)
    age_var.set(0)
    brand_var.set("")
    engine_var.set(0)
    continent_var.set("")
    engine_type_var.set("")
    color_entry.config(bg="#000000")
    root.configure(background='white')
root = tk.Tk()
root.title("Опитування про автомобіль")
data_frame = ttk.LabelFrame(root, text="Введіть попередні дані про автомобіль")
data_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
car_type_var = tk.IntVar()
new_car_check = ttk.Checkbutton(data_frame, text="Новий автомобіль", variable=car_type_var, onvalue=1, offvalue=0)
new_car_check.grid(row=0, column=0, padx=5, pady=5, sticky="w")
foreign_car_check = ttk.Checkbutton(data_frame, text="Іноземного виробництва", variable=car_type_var, onvalue=2, offvalue=0)
foreign_car_check.grid(row=1, column=0, padx=5, pady=5, sticky="w")
basic_questions_button = ttk.Button(root, text="Основні питання", command=clear_selection)
basic_questions_button.grid(row=0, column=2, padx=10, pady=5, sticky="e")
age_frame = ttk.LabelFrame(root, text="Скільки років?")
age_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
age_var = tk.IntVar()
age_options = [("До 5 років", 1), ("6-10 років", 2), ("11-15 років", 3), ("Більше 15 років", 4)]
for option, value in age_options:
    ttk.Radiobutton(age_frame, text=option, variable=age_var, value=value).pack(anchor="w", padx=5, pady=2)
brand_frame = ttk.LabelFrame(root, text="Марка автомобіля")
brand_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
brand_var = tk.StringVar()
brands = ["BMW", "Mercedes", "Volkswagen", "Mazda", "VAZ", "Інша"]
for i, brand in enumerate(brands):
    ttk.Radiobutton(brand_frame, text=brand, variable=brand_var, value=brand).pack(anchor="w", padx=5, pady=2)
engine_frame = ttk.LabelFrame(root, text="Об'єм двигуна")
engine_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
engine_var = tk.StringVar()
engine_options = [("Менше 1200", 1), ("1200-1500", 2), ("1501-2200", 3), ("Більше 2200", 4)]
for option, value in engine_options:
    ttk.Radiobutton(engine_frame, text=option, variable=engine_var, value=value).pack(anchor="w", padx=5, pady=2)
continent_frame = ttk.LabelFrame(root, text="Континент виробника")
continent_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
continent_var = tk.StringVar()
continents = ["Західна Європа", "Східна Європа", "Азія", "Америка"]
for i, continent in enumerate(continents):
    ttk.Radiobutton(continent_frame, text=continent, variable=continent_var, value=continent).pack(anchor="w", padx=5, pady=2)
engine_type_frame = ttk.LabelFrame(root, text="Вид двигуна")
engine_type_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
engine_type_var = tk.StringVar()
engine_type_options = [("Дизель", "Дизель"), ("Бензин", "Бензин")]
for option, value in engine_type_options:
    ttk.Radiobutton(engine_type_frame, text=option, variable=engine_type_var, value=value).pack(anchor="w", padx=5, pady=2)
color_frame = ttk.LabelFrame(root, text="Колір")
color_frame.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
color_button = ttk.Button(color_frame, text="Обрати колір", command=color)
color_button.pack()
color_entry = tk.Entry(color_frame, width=20)
color_entry.pack(side="left", padx=5, pady=2)
result_frame = ttk.LabelFrame(root, text="Результат вибору")
result_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
result_label = ttk.Label(result_frame, text="")
result_label.pack()
show_button = ttk.Button(root, text="Результат вибору", command=show_results)
show_button.grid(row=4, column=2, padx=10, pady=5, sticky="e")
clear_button = ttk.Button(root, text="Нове опитування", command=clear_selection)
clear_button.grid(row=4, column=1, padx=10, pady=5, sticky="w")
root.mainloop()