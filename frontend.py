from tkinter import font, ttk
import tkinter as tk

import backend as be

window = tk.Tk()
window.title("Shunting backyard")
window.geometry('500x250')

lbl1 = ttk.Label(window, text='Input format:')
lbl1.grid(column=0, row=0)

lbl2 = ttk.Label(window, text='Output format:')
lbl2.grid(column=0, row=1)

input_format = tk.StringVar()
output_format = tk.StringVar()

input_format.set('infix')
output_format.set('postfix')

input_options = [
    ttk.Radiobutton(window, text='infix', value='infix',
                   variable=input_format),
    ttk.Radiobutton(window, text='prefix', value='prefix', 
                   variable=input_format, state='disabled'),
    ttk.Radiobutton(window, text='postfix', value='postfix', 
                   variable=input_format),
]

output_options = [
    ttk.Radiobutton(window, text='infix', value='infix',
                   variable=output_format),
    ttk.Radiobutton(window, text='prefix', value='prefix', 
                   variable=output_format, state='disabled'),
    ttk.Radiobutton(window, text='postfix', value='postfix', 
                   variable=output_format),
]

for n, i in enumerate(input_options):
    i.grid(column=n+1, row=0)

for n, i in enumerate(output_options):
    i.grid(column=n+1, row=1)

lbl3 = ttk.Label(window, text="INPUT:")
lbl3.grid(column=0, row=2)
input_entry = ttk.Entry(window, width=50)
input_entry.grid(column=0, row=3)
input_entry.focus()

lbl4 = ttk.Label(window, text="OUTPUT:")
lbl4.grid(column=0, row=4)
output_label = ttk.Label(window, text='n/a')
output_label.grid(column=0, row=5)

def clicked():
    inp = input_entry.get()

    try:
        assert len(inp) > 0, "expression can't be empty"
        if input_format.get() == 'infix' and output_format.get() == 'postfix':
            result = be.infix2postfix(inp)
        elif input_format.get() == 'postfix' and output_format.get() == 'infix':
            result = be.postfix2infix(inp)
        elif input_format.get() == 'postfix' and output_format.get() == 'prefix':
            result = be.postfix2prefix(inp)
        else:
            result = f"WARNING: Can't convert from {input_format.get()} to {output_format.get()}"
    
    except Exception as e:
        result = f"ERROR: {e}"
    
    output_label.configure(text=result)

run_btn = ttk.Button(window, text="RUN", command=clicked)
run_btn.grid(column=0, row=6)


window.mainloop()
