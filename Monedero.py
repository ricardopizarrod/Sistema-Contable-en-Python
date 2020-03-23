# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
root=Tk()
root.state("zoomed")
root.title("Monedero - Sistema Contable")
#root.iconbitmap()
root.geometry("+0+0")

class Monedero():

	def salirApp():
		valor=messagebox.askokcancel("¡Atencion!, ¿Estás seguro que deseas salir?")
		if valor==True:
			root.destroy()

	def infoLicencia():
		messagebox.showwarning("Licencia", "Licencia Activada")

	def infoAcercaDe():
		messagebox.showinfo("Monedero", "Creado por: \nRicardo Pizarro \nCopyright ©℗®™ 2020")

	def InvoVersion():
		messagebox.showinfo("Version", "Version: 1.0.0 - Build: C0B010")

	def infoNovedades():
		miFrameNovedades=Toplevel()
		miFrameNovedades.title("Monedero - Sistema Contable - Novedades")
		#miFrameNovedades.iconbitmap(imagenes/wallet.ico)
		miFrameNovedades.geometry("+420+250")
		miFrameNovedades.config(bg="#1F1F1F")
		miFrameNovedades2=Frame(miFrameNovedades)
		miFrameNovedades2.pack(fill="both", expand="True")
		miFrameNovedades2.config(bg="#1F1F1F")
		miFrameNovedades2.config(width="1200", height="600")
		miFrameNovedades2.config(bd=15)
		miFrameNovedades2.config(relief="groove")

		tituloLabel=Label(miFrameNovedades2, text="NOVEDADES", bg="#1F1F1F", fg="#03f943")
		tituloLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
		cuadroNovedades=Text(miFrameNovedades2, width=60, height=15, bg="#1F1F1F", fg="#FFFFFF")
		cuadroNovedades.grid(row=1, column=0)
		scrollVertical=Scrollbar(miFrameNovedades2, command=cuadroNovedades.yview)
		scrollVertical.grid(row=1, column=1, sticky="nsew")

		cuadroNovedades.insert(INSERT, "\
			Version: 1.0.0\
			\n* Aqui la priemra novedad\
			\n* \
			\n* \
			\n* \
			\n* ")
		cuadroNovedades.config(yscrollcommand=scrollVertical.set, state="disable")



	barraMenu=Menu(root)
	root.config(menu=barraMenu, width=300, height=300)

	archivoMenu=Menu(barraMenu, tearoff=0)
	archivoMenu.add_command(label="Crear BBDD")
	archivoMenu.add_separator()
	archivoMenu.add_command(label="Salir", command=salirApp)

	contabilidadMenu=Menu(barraMenu, tearoff=0)
	contabilidadMenu.add_command(label="Deudas")
	contabilidadMenu.add_command(label="Prestamo")
	contabilidadMenu.add_command(label="General")
	contabilidadMenu.add_command(label="Banco")

	ayudaMenu=Menu(barraMenu, tearoff=0)
	ayudaMenu.add_command(label="Licencia", command=infoLicencia)
	ayudaMenu.add_command(label="Version", command=InvoVersion)
	ayudaMenu.add_command(label="Novedades", command=infoNovedades)
	ayudaMenu.add_command(label="Acerca de...", command=infoAcercaDe)

	barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
	barraMenu.add_cascade(label="Contabilidad", menu=contabilidadMenu)
	barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

	def login():
		miFrameLogin=Toplevel()
		miFrameLogin.title("Monedero - Sistema Contable - Acceso")
		#miFrameLogin.iconbitmap("imagenes/wallet.ico")
		miFrameLogin.geometry("+500+250")
		miFrameLogin.config(bg="#1F1F1F")
		miFrameLogin2=Frame(miFrameLogin)
		miFrameLogin2.pack(fill="both", expand="True")
		miFrameLogin2.config(bg="#1F1F1F")
		miFrameLogin2.config(width="1200", height="600")
		miFrameLogin2.config(bd=15)
		miFrameLogin2.config(relief="groove")

		def verificar():
			if miCuadroUsuario.get().upper() == "USER" and miCuadroClave.get().upper() == "1234":
				messagebox.showinfo(title = "Login Correcto", message = "Bienvenido" + miCuadroUsuario.get())
				miFrameLogin.destroy()
				root.iconify()
				root.deiconify()
			else:
				messagebox.showerror(title= "Login incorrecto", message ="Usuario o contraseña incorrecta")

		def salirLogin():
			root.destroy()

		miCuadroUsuario=StringVar()
		miCuadroClave=StringVar()



		labelUsuario=Label(miFrameLogin2, text="USUARIO", bg="#1F1F1F", fg="#03f943")
		labelUsuario.grid(row=0, column=0, sticky="e", padx=10, pady=10)
		CuadroUsuario=Entry(miFrameLogin2, textvariable=miCuadroUsuario)
		CuadroUsuario.grid(row=0, column=1, padx=10, pady=10)
		labelClave=Label(miFrameLogin2, text="CLAVE:", bg="#1F1F1F", fg="#03f943")
		labelClave.grid(row=1, column=0, sticky="w", padx=10, pady=10)
		cuadroClave=Entry(miFrameLogin2, show="*", textvariable=miCuadroClave)
		cuadroClave.grid(row=1, column=1, padx=10, pady=10)
		botonEntrar=Button(miFrameLogin2, text="Entrar", width=10, height=1, borderwidth=1, highlightbackground="#1F1F1F", command=verificar)
		botonEntrar.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

		cuadroClave.bind('<Return>', lambda x: verificar())
		miFrameLogin.protocol("WM_DELETE_WINDOW", salirLogin)
		miFrameLogin.mainLoop()


	miFrame=Frame(root)
	miFrame.pack(fill="both", expand="True")
	miFrame.config(bg="#1f1f1f")
	miFrame.config(width="1280", height="676")
	miFrame.config(bd=15)
	miFrame.config(relief="groove")

	imagenMonedero=PhotoImage(file="imagenes/Monedero.png")
	Label(miFrame, image=imagenMonedero, bg="#1f1f1f").place(x=95, y=70)
	imagenFondo=PhotoImage(file="imagenes/Fondo.png")
	Label(miFrame, image=imagenFondo, bg="#1f1f1f").place(x=0, y=250)

	root.withdraw()
	login()
	root.mainLoop()