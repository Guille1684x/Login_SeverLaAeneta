from tkinter import *
from model.registrar import docente

def registrar_Docente(mainView, parentView):
    regDocView = Toplevel(mainView)
    regDocView.geometry("400x500")
    regDocView.title("Registro Docente")
    regDocView.iconbitmap("tesis.ico")

    parentView.destroy()
    regDocView.grab_set()
    regDocView.transient(mainView)

    global nombreUsuario_entry
    global contrasenia_entry

    nombreUsuario_entry = StringVar()
    contrasenia_entry = StringVar()

    Label(regDocView,
        text="Por favor ingrese su informacion\n a continuación ", 
        bg="firebrick", 
        fg="white", 
        width="300", 
        height="3", 
        font=("Calibri", 12)).pack()
    
    Label(regDocView, text='').pack()

    Label(regDocView, text="NOMBRE").pack()
    nombreUsuario = Entry(regDocView)
    nombreUsuario.pack()
    Label(regDocView).pack()

    Label(regDocView, text="APPELLIDO").pack()
    apellido = Entry(regDocView)
    apellido.pack()
    Label(regDocView).pack()

    Label(regDocView, text="ESPECIALIDAD").pack()
    especialidad = Entry(regDocView)
    especialidad.pack()
    Label(regDocView).pack()

    Label(regDocView, text="CORREO").pack()
    correo = Entry(regDocView)
    correo.pack()
    Label(regDocView).pack()

    Label(regDocView, text="FACULTAD").pack()
    facultad = Entry(regDocView)
    facultad.pack()
    Label(regDocView).pack()

    Label(regDocView, text="CONTRASEÑA").pack()
    contraseña = Entry(regDocView)
    contraseña.pack()
    Label(regDocView).pack()

    Button(
        regDocView, 
        text="Registrar", 
        command=lambda: (
            docente(nombreUsuario.get(), apellido.get(), especialidad.get(), correo.get(), facultad.get(), contraseña.get()),
            regDocView.destroy())
        ).pack()