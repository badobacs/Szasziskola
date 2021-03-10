import tkinter as tk


class App(tk.Frame):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.pack()
        self.meret=6

        self.plusz_gomb = tk.Button(master=self)
        self.plusz_gomb["text"] = "+"
        self.plusz_gomb.pack()
        self.plusz_gomb["command"] = self.handle_plus_gomb_press

        self.meret_doboz = tk.Text()
        self.meret_doboz.config(state=tk.DISABLED)
        self.meret_doboz["height"]=1
        self.meret_doboz["width"]=2
        self.meret_doboz.pack()

        self.minusz_gomb = tk.Button(master=self)
        self.minusz_gomb["text"] = "-"
        self.minusz_gomb["command"] = self.handle_minusz_gomb_press
        self.minusz_gomb.pack()

        self.update_meret_doboz()
  

        self.feladvany_doboz=tk.Text(self)
        self.feladvany_doboz["height"]=1
        self.feladvany_doboz.bind("<KeyRelease>",self.handle_feladvany_change)
        self.feladvany_doboz.pack()

        self.hossz_megfelelo=tk.Label(master=self,text="hossz: 0")
        self.hossz_megfelelo.pack()

        self.minusz_gomb = tk.Button(master=self)
        self.minusz_gomb["text"] = "ellenorzes"
        self.minusz_gomb["command"] = self.handle_ellenorzes_press
        self.minusz_gomb.pack()

    def handle_feladvany_change(self, event):
        feldv=self.feladvany_doboz.get('1.0',tk.END).strip()
        self.hossz_megfelelo["text"]=f"hossz: {len(feldv)}"

    def handle_ellenorzes_press(self):
        root=tk.Tk()
        feldv=self.feladvany_doboz.get('1.0',tk.END).strip()
        text=""
        if len(feldv)==self.meret**2:
            text="Megfelelo a hosz"
        else:
            text=f"{self.meret**2-len(feldv)} karakter hiányzik"
        label=tk.Label(root,text=text)
        label.pack()


    def handle_plus_gomb_press(self):
        if self.meret<9:
            self.meret+=1
        self.update_meret_doboz()


    def handle_minusz_gomb_press(self):
        if self.meret>4:
            self.meret-=1
        self.update_meret_doboz()
    
        
    def update_meret_doboz(self):
        self.meret_doboz.config(state=tk.NORMAL)
        self.meret_doboz.delete('1.0')
        self.meret_doboz.insert('1.0',self.meret)
        self.meret_doboz.config(state=tk.DISABLED)


root = tk.Tk(className="Sudoku-ellenőrző")
root.geometry("540x210")
app = App()
app.mainloop()
