import random
import tkinter as tk


def randomColor():
    return random.choice(["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"])


i = 0
upClicked = False


def up():
    global i, upClicked
    i += 1

    updateBg()
    amountStr.set(i)
    upClicked = True


def down():
    global i, upClicked
    i -= 1

    updateBg()
    amountStr.set(i)
    upClicked = False


def updateBg():
    if i == 0:
        root.configure(bg='gray')
    elif i > 0:
        root.configure(bg='green')
    elif i < 0:
        root.configure(bg='red')


def triple(e):
    global i

    if upClicked:
        i *= 3
    else:
        i //= 3

    amountStr.set(i)


root = tk.Tk()
root.title('Clicker')
root.configure(bg='gray')

root.bind('+', lambda e: up())
root.bind('-', lambda e: down())
root.bind('<Up>', lambda e: up())
root.bind('<Down>', lambda e: down())
root.bind('<space>', triple)

amountStr = tk.IntVar(value=0)

button = tk.Button(text='Up', bg=randomColor(), fg=randomColor())
button.pack(pady=20, padx=20)
button.configure(command=up)

text = tk.Label(root, bg=randomColor(), fg=randomColor())
text.configure(textvariable=amountStr)

text.bind('<Enter>', lambda e: root.configure(bg='yellow'))
text.bind('<Leave>', lambda e: updateBg())
text.bind('<Double-Button-1>', triple)

text.pack()

button = tk.Button(text='Down', bg=randomColor(), fg=randomColor())
button.pack(pady=20, padx=20)
button.configure(command=down)

root.mainloop()
