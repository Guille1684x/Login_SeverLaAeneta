from tkinter import *
from model.registrar import alumno


def registrar_Estudiante(mainView, parentView):
    regEstView = Toplevel(mainView)
    regEstView.geometry("400x450")
    regEstView.title("Registro Estudiante")
    regEstView.iconbitmap("tesis.ico")

    parentView.destroy()
    regEstView.grab_set()
    regEstView.transient(mainView)

    global nombreUsuario_entry
    global contrasenia_entry

    nombreUsuario_entry = StringVar()
    contrasenia_entry = StringVar()

    Label(regEstView,
        text="Por favor ingrese su informacion\n a continuación ", 
        bg="firebrick", 
        fg="white", 
        width="300", 
        height="3", 
        font=("Calibri", 12)).pack()
    
    Label(regEstView, text='').pack()

    Label(regEstView, text="NOMBRE").pack()
    nombreUsuario = Entry(regEstView)
    nombreUsuario.pack()
    Label(regEstView).pack()

    Label(regEstView, text="APPELLIDO").pack()
    apellido = Entry(regEstView)
    apellido.pack()
    Label(regEstView).pack()

    Label(regEstView, text="CORREO").pack()
    correo = Entry(regEstView)
    correo.pack()
    Label(regEstView).pack()

    Label(regEstView, text="FACULTAD").pack()
    facultad = Entry(regEstView)
    facultad.pack()
    Label(regEstView).pack()

    Label(regEstView, text="CONTRASEÑA").pack()
    contraseña = Entry(regEstView)
    contraseña.pack()
    Label(regEstView).pack()

    Button(regEstView, 
           text="Registrar", 
           command=lambda: (
               alumno(nombreUsuario.get(), apellido.get(), correo.get(), facultad.get(), contraseña.get()), 
               regEstView.destroy()
            )
        ).pack()