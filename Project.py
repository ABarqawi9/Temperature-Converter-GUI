import tkinter as tk

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        
        self.conversion_type_var = tk.StringVar(root)
        self.conversion_type_var.set("Celsius to Fahrenheit") 
        self.conversion_type_menu = tk.OptionMenu(root, self.conversion_type_var, "Celsius to Fahrenheit", "Fahrenheit to Celsius")
        self.conversion_type_menu.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.lbl_input = tk.Label(root, text="Input:")
        self.lbl_input.grid(row=1, column=0, padx=10, pady=10)

        self.entry_input = tk.Entry(root)
        self.entry_input.grid(row=1, column=1, padx=10, pady=10)

        self.lbl_result = tk.Label(root, text="Result:")
        self.lbl_result.grid(row=2, column=0, padx=10, pady=10)

        self.lbl_result_value = tk.Label(root, text="")
        self.lbl_result_value.grid(row=2, column=1, padx=10, pady=10)

        self.button_convert = tk.Button(root, text="Convert", command=self.convert_temperature)
        self.button_convert.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.button_clear = tk.Button(root, text="Clear", command=self.clear_all)
        self.button_clear.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.lbl_result.config(bg="white")

    def convert_temperature(self):
        try:
            input_value = float(self.entry_input.get())
            conversion_type = self.conversion_type_var.get()

            if conversion_type == "Celsius to Fahrenheit":
                result = input_value * 9/5 + 32
                self.lbl_result_value.config(text=f"{result:.2f} °F")
                if input_value <= 25:
                    self.lbl_result.config(bg="green")
                else:
                    self.lbl_result.config(bg="red")
            else: 
                result = (input_value - 32) * 5/9
                self.lbl_result_value.config(text=f"{result:.2f} °C")
                if result <= 25:
                    self.lbl_result.config(bg="green")
                else:
                    self.lbl_result.config(bg="red")

        except ValueError:
            self.lbl_result_value.config(text="Invalid input")

    def clear_all(self):
        self.entry_input.delete(0, tk.END)
        self.lbl_result_value.config(text="")
        self.lbl_result.config(bg="white")

root = tk.Tk()
app = TemperatureConverter(root)
root.mainloop()