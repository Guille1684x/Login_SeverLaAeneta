import tkinter
from tkinter import *
from tkinter import messagebox

import pymysql


def menu_pantalla():

    # Configuración inicial de la ventana
    global pantalla
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

    Label(text="Acceso al sistema", 
        bg="firebrick", 
        fg="white", 
        width="300", 
        height="3", 
        font=("Calibri", 15)).pack()

    Label(text="")

    # Botones

    Label(text="\n\n").pack()

    Button(text="Iniciar sesión",
        height="3",
        width="30",
        command=inicio_sesion).pack()

    Label(text="").pack()

    Button(text="Registrar",
        height="3",
        width="30",
        command=registrar).pack()

    # Loop
    pantalla.mainloop()

def inicio_sesion():
    global pantalla1 
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de sesión")
    pantalla1.iconbitmap("tesis.ico")

    Label(pantalla1,
          text="Por favor ingrese su usuario y contraseña\n a continuación", 
          bg="firebrick", 
          fg="white", 
          width="300", 
          height="3", 
          font=("Calibri", 12)).pack()
    
    Label(pantalla1, text="").pack()

    # Variables

    global nombreUsuario_verify
    global contraseniaUsuario_verify

    nombreUsuario_verify = StringVar()
    contraseniaUsuario_verify = StringVar()

    global nombre_usuario_entry
    global contrasenia_usuario_entry

    # Label

    Label(text="\n").pack()

    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable=nombreUsuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasenia_usuario_entry = Entry(pantalla1, show='*', textvariable=contraseniaUsuario_verify)
    contrasenia_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar sesión").pack()

def registrar():
    global pantalla2
    pantalla2 = Toplevel(pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("Registro")
    pantalla2.iconbitmap("tesis.ico")

    global nombreUsuario_entry
    global contrasenia_entry

    nombreUsuario_entry = StringVar()
    contrasenia_entry = StringVar()

    Label(pantalla2,
        text="Por favor ingrese un Usuario y Contraseña\n a continuación ", 
        bg="firebrick", 
        fg="white", 
        width="300", 
        height="3", 
        font=("Calibri", 12)).pack()
    
    Label(pantalla2, text='').pack()

    Label(pantalla2, text="Usuario").pack()
    nombreUsuario_entry = Entry(pantalla2)
    nombreUsuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Contraseña").pack()
    contrasenia_entry = Entry(pantalla2, show='*')
    contrasenia_entry.pack()
    Label(pantalla2).pack()

    Button(pantalla2, text="Registrar", command=inserta_datos).pack()

def inserta_datos():
    bd = pymysql.connect(
        host="localhost",
        user="admin",
        passwd='cola',
        db="bd_severlaaeneta"
    )

    fcursor = bd.cursor()

    sql = "INSERT INTO login (usuario, contrasena) VALUES ('{0}', '{1}')".format(nombreUsuario_entry.get(), contrasenia_entry.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message='Registro exitoso', title="Aviso")

    except:
        bd.rollback()
        messagebox.showinfo(message='No registrado', title="Aviso")

    bd.close()

menu_pantalla()




