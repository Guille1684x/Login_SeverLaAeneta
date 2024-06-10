from tkinter import *
from model.read import Read
from views.notify import notify

def log_alumno(parentView, mainView):
    logAlumView = Toplevel(mainView)
    logAlumView.geometry("400x250")
    logAlumView.title("Inicio de sesión")
    logAlumView.iconbitmap("tesis.ico")

    parentView.destroy()
    logAlumView.grab_set()
    logAlumView.transient(mainView)

    Label(logAlumView,
          text="Por favor ingrese su usuario y contraseña\n a continuación", 
          bg="firebrick", 
          fg="white", 
          width="300", 
          height="3", 
          font=("Calibri", 12)).pack()
    
    Label(logAlumView, text="").pack()

    # Variables

    nombreUsuario_verify = StringVar()
    contraseniaUsuario_verify = StringVar()

    # Label

    Label(text="\n").pack()

    Label(logAlumView, text="Usuario").pack()
    usuario = Entry(logAlumView, textvariable=nombreUsuario_verify)
    usuario.pack()
    Label(logAlumView).pack()

    Label(logAlumView, text="Contraseña").pack()
    contrasenia = Entry(logAlumView, show='*', textvariable=contraseniaUsuario_verify)
    contrasenia.pack()
    Label(logAlumView).pack()

    Button(logAlumView, text="Iniciar sesión", command=lambda: verify(usuario=usuario.get(), contrasenia=contrasenia.get())).pack()
    pass

def verify(usuario, contrasenia):
    read = Read()

    read.alumnos(usuario, contrasenia)
    result = read.get_result()

    if result:
        print("Usuario encontrado")
    else:
        print("No se ah encontrado el usuario")
        notify("Usuario o contraseña incorrectos!!")
