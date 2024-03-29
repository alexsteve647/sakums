import sqlite3
import tkinter as tk

savienojums = sqlite3.connect("majas_biblioteka.db")

kursors = savienojums.cursor()

class majas_Biblioteka:
    def __init__(self, autors, gramatas_nosaukums, publicesanas_gads, kategorija, gramatu_saraksts) -> None:
            self.autors = autors
            self.gramatas_nosaukums = gramatas_nosaukums
            self.publicesanas_gads = publicesanas_gads
            self.kategorija = kategorija
            self.gramatu_saraksts = gramatu_saraksts

    def pievienot_gramatu():
        print("Grāmata pievienota")

    def izdzest_gramatu():
        print("Grāmata tika izdzēsta")

    def apskatit_gramatas():
        print("Grāmata tika izdzēsta")

def pievienot():
    l_virsraksts.place_forget()
    b_pievienot_gramatu.place_forget()
    b_izdzest_gramatu.place_forget()
    b_apskatit_gramatas.place_forget()

def izdzest():
    l_virsraksts.place_forget()
    b_pievienot_gramatu.place_forget()
    b_izdzest_gramatu.place_forget()
    b_apskatit_gramatas.place_forget()

def apskatit():
    l_virsraksts.place_forget()
    b_pievienot_gramatu.place_forget()
    b_izdzest_gramatu.place_forget()
    b_apskatit_gramatas.place_forget()

root = tk.Tk()
root.title("Mājas bibliotēka")
root.geometry("500x400")
root.resizable(0,0)

l_virsraksts = tk.Label(root, text='Sveicināti Mājas bibliotēkā', font=('Calibri', 26, 'bold'), fg="red")

b_pievienot_gramatu = tk.Button(root, text="Pievienot grāmatu", height= 1, width=15, command=pievienot)

b_izdzest_gramatu = tk.Button(root, text="Izdzēst grāmatu", height= 1, width=15, command=izdzest)

b_apskatit_gramatas = tk.Button(root, text="Apskatīt grāmatas", height= 1, width=15, command=apskatit)


l_gramatas_nosaukums = tk.Label(root, text='Grāmatas nosaukums:', font=(15), fg="red")
l_gramatas_nosaukums.place(x=180, y=30)

e_gramatas_nosaukums = tk.Entry(root)
e_gramatas_nosaukums.place(x=192.5, y=50)

l_gramatas_autors = tk.Label(root, text='Grāmatas autors:', font=(15), fg="red")
l_gramatas_autors.place(x=180, y=90)

e_gramatas_publicesanas_gads = tk.Entry(root)
e_gramatas_publicesanas_gads.place(x=192.5, y=130)

l_gramatas_publicesanas_gads = tk.Label(root, text='Grāmatas publicēšanas gads:', font=(15), fg="red")
l_gramatas_publicesanas_gads.place(x=180, y=150)

e_gramatas_nosaukums = tk.Entry(root)
e_gramatas_nosaukums.place(x=192.5, y=170)

l_gramatas_kategorija = tk.Label(root, text='Grāmatas kategorija:', font=(15), fg="red")
l_gramatas_kategorija.place(x=180, y=210)

e_gramatas_kategorija= tk.Entry(root)
e_gramatas_kategorija.place(x=192.5, y=230)

# l_virsraksts.place(x=50, y=30)
# b_pievienot_gramatu.place(x=192.5, y=100)
# b_izdzest_gramatu.place(x=192.5, y=130)
# b_apskatit_gramatas.place(x=192.5, y=160)


root.mainloop()
