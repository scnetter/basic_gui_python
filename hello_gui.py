import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text = "Hello, Tkinter")
greeting.pack()

button = tk.Button(
    text="Click Me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()

window.mainloop()