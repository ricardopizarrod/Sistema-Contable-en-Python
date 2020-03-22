from tkinter import *
root=Tk()
root.state("zoomed")
root.title("Monedero - Sistema Contable")
#root.iconbitmap()
root.geometry("+0+0")

class Monedero():
	barraMenu=Menu(root)
	root.config(menu=barraMenu, width=300, height=300)

	archivoMenu=Menu(barraMenu, tearoff=0)
	archivoMenu.add_command(label="Crear BBDD")
	archivoMenu.add_separator()
	archivoMenu.add_command(label="Salir")

	contabilidadMenu=Menu(barraMenu, tearoff=0)
	contabilidadMenu.add_command(label="Deudas")
	contabilidadMenu.add_command(label="Prestamo")
	contabilidadMenu.add_command(label="General")
	contabilidadMenu.add_command(label="Banco")

	ayudaMenu=Menu(barraMenu, tearoff=0)
	ayudaMenu.add_command(label="Licencia")
	ayudaMenu.add_command(label="Version")
	ayudaMenu.add_command(label="Novedades")
	ayudaMenu.add_command(label="Acerca de...")

	barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
	barraMenu.add_cascade(label="Contabilidad", menu=contabilidadMenu)
	barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)	

	miFrame=Frame(root)
	miFrame.pack(fill="both", expand="True")
	miFrame.config(bg="#1f1f1f")
	miFrame.config(width="1280", height="676")
	miFrame.config(bd=15)
	miFrame.config(relief="groove")

	root.mainLoop()