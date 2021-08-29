from tkinter import *
from tkinter import ttk
root = Tk()
root.title('Convert Text to Binary')
root.iconbitmap('assets/spaceship_red.ico')
root.geometry('800x450')
root.resizable(False, False)
root.config(bg='#252526')
f = 'Helvetica'
b = '#252526'
fg = 'SystemButtonFace'
tab = ttk.Notebook()
tab.pack(side=TOP)
t = Frame(root, width=800, height=450, background='#252526')
t.pack(fill=BOTH)
f = Frame(root, width=800, height=450, background='#252526')
f.pack(fill=BOTH)
f.pack_propagate(0)
t.pack_propagate(0)
tab.add(t, text='Convert Text to Binary')
tab.add(f, text='Convert Binary to Text')
def fken(e):
	text.config(state=NORMAL)
	text.delete(1.0, END)
def reset():
	p.pack_forget()
	text.config(height=8)
	submit.config(command=convert, text='Convert')
def convert():
	global p
	submit.config(command=reset, text='Reset')
	string = text.get(1.0, END)
	text.config(height=1)
	if string == 'Enter Text to Convert to Binary':
		submit.pack(pady=20)
	else:
		binary_converted = ' '.join(format(c, 'b') for c in bytearray(string, "utf-8"))
		p = Text(t, font=(f, 12))
		p.pack(pady=(15, 0))
		p.insert(1.0, binary_converted)
		p.config(state=DISABLED)
trib = Label(t, text='Convert To Binary', font=(f, 27), bg=b, fg=fg)
trib.pack(pady=5)
text = Text(t, width=35, font=(f, 15), height=8)
text.pack(pady=20)
text.insert(1.0, 'Enter Text to Convert to Binary')
text.config(state=DISABLED)
submit = Button(t, text='Convert', font=(f, 13), command=convert)
submit.pack(pady=(5, 20))
text.bind("<Button-1>", fken)
def fkene(e):
	text1.config(state=NORMAL)
	text1.delete(1.0, END)
def resete():
	pp.pack_forget()
	text1.config(height=8)
	submit1.config(command=convertt, text='Convert')
def convertt():
	global pp
	submit1.config(command=resete, text='Reset')
	strings = text.get(1.0, END)
	text1.config(height=1)
	if strings == 'Enter Binary to Convert to Text':
		submit1.pack(pady=20)
	else:
		a_binary_string = text1.get(1.0, END)
		binary_values = a_binary_string.split()
		ascii_string = ""
		for binary_value in binary_values:
			an_integer = int(binary_value, 2)
			ascii_character = chr(an_integer)
			ascii_string += ascii_character
		pp = Text(f, font=(f, 12))
		pp.pack(pady=(15, 0))
		pp.insert(1.0, ascii_string)
		pp.config(state=DISABLED)
trib1 = Label(f, text='Convert To Text', font=(f, 27), bg=b, fg=fg)
trib1.pack(pady=5)
text1 = Text(f, width=35, font=(f, 15), height=8)
text1.pack(pady=20)
text1.insert(1.0, 'Enter Binary to Convert to Text')
text1.config(state=DISABLED)
submit1 = Button(f, text='Convert', font=(f, 13), command=convertt)
submit1.pack(pady=(5, 20))
text1.bind("<Button-1>", fkene)
root.mainloop()