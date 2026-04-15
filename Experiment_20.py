import tkinter as tk

def convert():
    try:
        value = float(entry.get())
        choice = option.get()
        print(value, choice)

        if choice == "celsius to fahrenheit":
            result = (value * 9/5) + 32
            output.config(text="result: " + str(result) + " F")

        elif choice == "rupees to dollars":
            result = value / 83
            output.config(text="result: $ " + str(round(result, 2)))

        elif choice == "inches to feet":
            result = value / 12
            output.config(text="result: " + str(result) + " ft")

    except:
        output.config(text="enter valid number!")

root = tk.Tk()
root.title("unit converter app")
root.geometry("350x300")

tk.Label(root, text="unit converter", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="enter value").pack()
entry = tk.Entry(root)
entry.pack(pady=5)

option = tk.StringVar()
option.set("celsius to fahrenheit")

menu = tk.OptionMenu(root, option,
                     "celsius to fahrenheit",
                     "rupees to dollars",
                     "inches to feet")
menu.pack(pady=10)

tk.Button(root, text="convert", command=convert).pack(pady=10)

output = tk.Label(root, text="result will appear here")
output.pack(pady=10)

root.mainloop()
