from tkinter import *
from views.log_alumno import log_alumno
from views.log_docente import log_docente

def login(mainView):
    pantallaLog = Toplevel(mainView)
    pantallaLog.geometry("300x150")
    pantallaLog.title("Seleccionar Tipo de Usuario")
    pantallaLog.geometry("180x200")

    pantallaLog.grab_set()
    pantallaLog.transient(mainView)

    Label(pantallaLog,
        text="Que tipo de usuario \neres?", 
        bg="firebrick", 
        fg="white", 
        width="100", 
        height="4", 
        font=("Calibri", 12)).pack()

    # Funciones para cada botón
    estudiante_cmd = lambda: log_alumno(pantallaLog, mainView)
    docente_cmd = lambda: log_docente(pantallaLog, mainView)

    
    Label(text="\n\n").pack()

    # Botón para Estudiante
    btn_estudiante = Button(pantallaLog, text="Estudiante", command=estudiante_cmd, width="8", height="2")
    btn_estudiante.pack(side=LEFT, padx=10)

    # Botón para Docente
    btn_docente = Button(pantallaLog, text="Docente", command=docente_cmd, width="8", height="2")
    btn_docente.pack(side=LEFT, padx=10)

    pantallaLog.mainloop()