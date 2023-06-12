#GUI - Graphical User Interface
# Tkinter - Tk Interface
# import el modulo de tkinter

import tkinter as tk
# Importamos el modulo del tema de tkinter
from tkinter import ttk


#Creamos un objeto usando la clase Tk
ventana = tk.Tk()
#Modificamos el tamaño de la ventana (pixeles)
ventana.geometry('800x800')
#Cambiamos el nombre de la ventana
ventana.title('Hola mundo  ')
#Configuramos el icono de la aplicacion
ventana.iconbitmap('icono.ico')
#Creamos un metodo evento_click
def evento_click():
    boton1.config(text='Boton presionando')
    print('Ejecucion del evento_click')
    #Creamos un nuevo boton y lo mostramos
    boton2 = ttk.Button(ventana, text='Nuevo botón')
    boton2.pack()

#Creamos un boton (widget), el objeto padre es ventana
boton1 = ttk.Button(ventana, text='Galletas', command=evento_click)
#Utilizar el pack layout manager para mostrar el boton de la ventana
boton1.pack()

#Iniciamos la ventana (esta linea la ejecutamos al final)
#Si la ejecutamos antes, no se muestran los cambios anteriores
ventana.mainloop()

