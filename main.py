from tkinter import *
from tkinter import ttk


class toDo:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDoList")
        self.root.geometry('500x400+300+150')

        self.label = Label(self.root, text="ToDoList", width=10, bd=2, bg='green', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.add = Label(self.root, text="AddTask", width=10, bd=2, bg='green', fg='black')
        self.add.place(x=85, y=40)

        self.tasks = Label(self.root, text="Tasks", width=10, bd=2, bg='green', fg='black')
        self.tasks.place(x=300, y=40)

        self.main_text = Listbox(self.root, height=15, width=20, bd=5)
        self.main_text.place(x=250, y=70)

        self.text = Text(self.root, bd=5, height=2, width=30)
        self.text.place(x=20, y=70)

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'w') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt', 'r+') as f:
                new_file = f.readlines()
                f.seek(0)
                for line in new_file:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        with open('data.txt', 'r') as file:
            read = file.readlines()
            for line in read:
                ready = line.split()
                self.main_text.insert(END, ready)
            file.close()

        self.button_add = Button(self.root, text='Add', width=10, bd=2, bg='green', fg='black', command=add)
        self.button_add.place(x=70, y=120)

        self.button_del = Button(self.root, text='Delete', width=10, bd=2, bg='green', fg='black', command=delete)
        self.button_del.place(x=70, y=150)


def main():
    root = Tk()
    ui = toDo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
