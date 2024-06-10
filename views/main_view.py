from tkinter import *
from views.register import registrar
from views.login import login

def main_window():

    # Configuración inicial de la ventana
    pantalla = Tk()
    pantalla.geometry("500x400")
    pantalla.title("Bienvenidos")
    pantalla.iconbitmap("tesis.ico")

    # Configuración del título

    image = PhotoImage(file="Sever La Aeneta.gif")
    image = image.subsample(2,2)
    label = Label(image=image)
    label.pack()

    # Label principal

    Label(pantalla,
        text="Acceso al sistema", 
        bg="firebrick", 
        fg="white", 
        width="300", 
        height="3", 
        font=("Calibri", 15)
    ).pack()

    Label(pantalla, text="")

    # Botones

    Label(pantalla, text="\n\n").pack()

    Button(pantalla, 
        text="Iniciar sesión",
        height="3",
        width="30",
        command=lambda: login(mainView=pantalla)).pack()

    Label(pantalla, text="").pack()

    Button(pantalla,
        text="Registrar",
        height="3",
        width="30",
        command=lambda: registrar(mainView=pantalla)).pack()

    # Loop
    pantalla.mainloop()