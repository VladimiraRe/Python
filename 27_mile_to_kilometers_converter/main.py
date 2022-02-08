from tkinter import *


def calculate():
    if radio_state.get() == 1:
        m = float(entry.get())
        answer = round(m * 1.609344, 2)
        result["text"] = answer
    else:
        m = float(entry.get())
        answer = round(m / 1.609344, 2)
        result["text"] = answer


def choice_1():
    entry_label["text"] = "miles"
    result_label["text"] = "km"


def choice_2():
    entry_label["text"] = "km"
    result_label["text"] = "miles"


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=40, pady=40)

entry = Entry(width=10)
entry.insert(END, string="")
entry.grid(column=0, row=1)

entry_label = Label(text="")
entry_label.grid(column=0, row=2)

radio_state = IntVar()
m_to_km = Radiobutton(text="miles to km", value=1,
                      variable=radio_state,
                      command=choice_1)
m_to_km.grid(column=0, row=0)

km_to_m = Radiobutton(text="km to miles", value=2,
                      variable=radio_state,
                      command=choice_2)
km_to_m.grid(column=2, row=0)

equal_label = Label(text="=", font=("Arial", 20, "normal"))
equal_label.grid(column=1, row=1)

result = Label(text="", font=("Arial", 20, "normal"))
result.grid(column=2, row=1)

result_label = Label(text="")
result_label.grid(column=2, row=2)

button = Button(text="Calculate", font=("Arial", 20, "normal"),
                command=calculate)
button.grid(column=1, row=3)

window.mainloop()


