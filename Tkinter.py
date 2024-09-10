from tkinter import Tk, Label, Button, Entry, END

root = Tk()
root.title("Ma première fenêtre")
root.geometry("500x500")

# Ajouter un texte large
label = Label(root, text="Hello World!", font=("Helvetica", 32))

# Ajouter le texte à la fenetre
label.pack()

# Ajouter un texte plus petit
label2 = Label(root, text="Hello World!", font=("Helvetica", 16))
label2.pack()

label3 = Label(root, text="Votre nom", font=("Helvetica", 16))
label3.pack()

entry = Entry(root)
entry.pack()


def btn_click_nom():
    label3.config(text=entry.get())
    entry.delete(0, END)
    label3.pack()


button4 = Button(root, text="Valider", command=btn_click_nom)
button4.pack()

# Ajoutons un bouton
button = Button(root, text="Click Me!")
button.pack()


# Ajoutons un action au bouton
def action():
    print("Vous avez cliqué !")


button2 = Button(root, text="Click Me!", command=action)
button2.pack()


# Ajoutons un action au boutton qui change le texte
def action2():
    label2.config(text="Vous avez cliqué !")
    label2.pack()


button3 = Button(root, text="Click Me!", command=action2)
button3.pack()

root.mainloop()
