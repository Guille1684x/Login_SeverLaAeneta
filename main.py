from views.main_view import main_window

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

main_window()



