import tkinter as tk


class App(tk.Frame):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.pack()

        self.masik_gomb = tk.Button(master=self)
        self.masik_gomb["text"] = "Right"
        self.masik_gomb.pack(side=tk.RIGHT)

        self.hello_gomb = tk.Button(master=self)
        self.hello_gomb["text"] = "Hello"
        self.hello_gomb["command"] = self.handle_hello_button_press
        self.hello_gomb.pack(side=tk.LEFT)

        self.szoveg_doboz = tk.Text()
        self.szoveg_doboz.pack()

    def handle_hello_button_press(self):
        print(self.szoveg_doboz.get("1.0", tk.END))


root = tk.Tk()
app = App()
app.mainloop()
