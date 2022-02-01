import random
import tkinter as tk


def randomColor():
    return random.choice(["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"])


i = 0


def up():
    global i
    i += 1

    updateBg()
    amountStr.set(i)


def down():
    global i
    i -= 1

    updateBg()
    amountStr.set(i)


def updateBg():
    if i == 0:
        root.configure(bg='gray')
    elif i > 0:
        root.configure(bg='green')
    elif i < 0:
        root.configure(bg='red')


root = tk.Tk()
root.title('Clicker')
root.configure(bg='gray')

amountStr = tk.IntVar(value=0)

button = tk.Button(text='Up', bg=randomColor(), fg=randomColor())
button.pack(pady=20, padx=20)
button.configure(command=up)

text = tk.Label(root, bg=randomColor(), fg=randomColor())
text.configure(textvariable=amountStr)

text.bind('<Enter>', lambda e: root.configure(bg='yellow'))
text.bind('<Leave>', lambda e: updateBg())

text.pack()

button = tk.Button(text='Down', bg=randomColor(), fg=randomColor())
button.pack(pady=20, padx=20)
button.configure(command=down)

root.mainloop()
