import tkinter as tk
from tkinter import scrolledtext
import re

#functions list
def set_input(obj, value):
    obj.delete(1.0, tk.END)
    obj.insert(tk.END, value)

def reverse():
    scr.config(state='normal')
    temp = e.get("1.0","end-1c")
    temp = re.findall(r'[\w]+', temp)
    if len(temp) > 1:
        temp = temp[::-1]
        set_input(scr, ' '.join(temp))
    elif len(temp) == 1:
        set_input(scr, temp[0][::-1])
    scr.config(state='disabled')
        
#window config
window = tk.Tk()
window.title('Reverse a String')
window.geometry('300x210')

#window content
scr = scrolledtext.ScrolledText(window, state='disabled',
             width=300, height=6, bg='#9eedad',
             font=('Arial', 12), wrap=tk.WORD)
scr.pack()

e = tk.Text(window, width=300, height=4)
e.pack()

b = tk.Button(window, width=150, height=2, text='Reverse them', command=reverse)
b.pack()


#window start
window.mainloop()
