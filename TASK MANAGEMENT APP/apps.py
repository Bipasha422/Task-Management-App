import tkinter as tk
root = tk.Tk ()
root.title("To do list App")
root.configure(bg="#f4f6f7")
root.geometry("600x400")
lb1=tk.Label(root,text="Enter task:",font=('calibari',15),bg="#f4f6f7",fg="#2c3e50")
lb1.place(x=5,y=15)
ent=tk.Entry(root,width=40,bg="white",fg="black",font=('calibari',12))
ent.place(x=100,y=20)
lbox=tk.Listbox(root,width=40,height=10,bg="white",fg="black",selectbackground="#1abc9c",selectforeground="white")
lbox.place(x=100,y=70)
def add_command():
    task=ent.get()
    if task != "":
        lbox.insert(tk.END,task)
        ent.delete(0, tk.END)
btn1=tk.Button(root,text="ADD",font=('calibari',15),width=10,bg="#2ecc71",fg="white",activebackground="#27ae60",command=add_command)
btn1.place(x=30,y=250)
def remove_command():
    try:
        selected = lbox.curselection()[0] 
        lbox.delete(selected)
    except IndexError:
       pass
btn2=tk.Button(root,text="REMOVE",font=('calibari',15),width=10,bg="#e74c3c",fg="white",activebackground="#c0392b",command=remove_command)
btn2.place(x=160,y=250)
def update_command():
    try:
        selected = lbox.curselection()[0]
        new_task = ent.get()
        if new_task != "":
            lbox.delete(selected)
            lbox.insert(selected,new_task)
            ent.delete(0, tk.END)
    except IndexError:
        pass       

btn3=tk.Button(root,text="UPDATE",font=('calibari',15),width=10,bg="#3498db",fg="white",activebackground="#2980b9",command=update_command)
btn3.place(x=290,y=250)
def mark_command():
    try:
        selected = lbox.curselection()[0]
        task = lbox.get(selected)
        if not task.startswith("*"):
            lbox.delete(selected)
            lbox.insert(selected, "*"+ task)
    except IndexError:
        pass        
btn4=tk.Button(root,text="MARK",font=('calibari',15),width=10,bg="#9b59b6",fg="white",activebackground="#8e44ad",command=mark_command)
btn4.place(x=420,y=250)





root.mainloop()