from tkinter import *
from model.read import Read
from views.notify import notify

def log_docente(parentView, mainView):
    logDocView = Toplevel(mainView)
    logDocView.geometry("400x250")
    logDocView.title("Inicio de sesión")
    logDocView.iconbitmap("tesis.ico")

    parentView.destroy()
    logDocView.grab_set()
    logDocView.transient(mainView)

    Label(logDocView,
          text="Por favor ingrese su usuario y contraseña\n a continuación", 
          bg="firebrick", 
          fg="white", 
          width="300", 
          height="3", 
          font=("Calibri", 12)).pack()
    
    Label(logDocView, text="").pack()

    # Variables

    nombreUsuario_verify = StringVar()
    contraseniaUsuario_verify = StringVar()

    # Label

    Label(text="\n").pack()

    Label(logDocView, text="Usuario").pack()
    usuario = Entry(logDocView, textvariable=nombreUsuario_verify)
    usuario.pack()
    Label(logDocView).pack()

    Label(logDocView, text="Contraseña").pack()
    contrasenia = Entry(logDocView, show='*', textvariable=contraseniaUsuario_verify)
    contrasenia.pack()
    Label(logDocView).pack()

    Button(logDocView, text="Iniciar sesión", command=lambda: verify(usuario=usuario.get(), contrasenia=contrasenia.get())).pack()
    pass

def verify(usuario, contrasenia):
    read = Read()

    read.docente(usuario, contrasenia)
    result = read.get_result()

    if result:
        print("Usuario encontrado")
    else:
        print("No se ah encontrado el usuario")
        notify("Usuario o contraseña incorrectos!!")
