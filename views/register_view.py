from tkinter import *
from views.reg_alumno_view import registrar_Estudiante
from views.reg_docente_view import registrar_Docente

def registrar(mainView):
    pantallaReg = Toplevel(mainView)
    pantallaReg.geometry("300x150")
    pantallaReg.title("Seleccionar Tipo de Usuario")
    pantallaReg.geometry("180x200")

    pantallaReg.grab_set()
    pantallaReg.transient(mainView)

    Label(pantallaReg,
        text="Que tipo de usuario \ndesea registrar?", 
        bg="firebrick", 
        fg="white", 
        width="100", 
        height="4", 
        font=("Calibri", 12)).pack()

    # Funciones para cada botón
    estudiante_cmd = lambda: registrar_Estudiante(mainView=mainView, parentView=pantallaReg)
    docente_cmd = lambda: registrar_Docente(mainView=mainView, parentView=pantallaReg)

    
    Label(text="\n\n").pack()

    # Botón para Estudiante
    btn_estudiante = Button(pantallaReg, text="Estudiante", command=estudiante_cmd, width="8", height="2")
    btn_estudiante.pack(side=LEFT, padx=10)

    # Botón para Docente
    btn_docente = Button(pantallaReg, text="Docente", command=docente_cmd, width="8", height="2")
    btn_docente.pack(side=LEFT, padx=10)

    pantallaReg.mainloop()