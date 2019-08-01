import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there['text'] = 'Hello World\n(clique-me)'
        self.hi_there['command'] = self.say_hi
        self.hi_there.pack(side='bottom')
        self.sair = tk.Button(self)
        self.sair['text'] = 'Sair'
        self.sair['command'] = self.sair.quit
        self.sair.pack()

    def say_hi(self):
        print('E aí pessoal!!!!')



root = tk.Tk()
app = Application(master=root)
app.mainloop()
