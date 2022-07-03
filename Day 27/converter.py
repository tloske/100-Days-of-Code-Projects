import tkinter


def convert_to_kilometers():
    result_label.config(text=f"{float(input.get()) * 1.609}")


window = tkinter.Tk()
window.title = ("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

input = tkinter.Entry(width=7)
input.grid(column=1, row=0)

input_label = tkinter.Label(text="Miles", font=("Arial", 12))
input_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 12))
is_equal_label.grid(column=0, row=1)

result_label = tkinter.Label(text=0, font=("Arial", 12))
result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=convert_to_kilometers)
button.grid(column=1, row=2)

window.mainloop()
