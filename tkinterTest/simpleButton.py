from tkinter import Tk, Button

count = 0 #Records the number of the button presses

def update():
    count = 0
    global count, b
    count += 1
    b.config(text="Click count = " + str(count))
    print("Updating")

root = Tk()
b = Button(root)
b.configure(background="yellow", text="Click count = 0", command=update)
b.pack()
root.mainloop()

