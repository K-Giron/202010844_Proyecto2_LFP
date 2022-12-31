from tkinter import *
from tkinter import ttk,filedialog
import tkinter as tk
from tkinter import messagebox as MessageBox
from Gramaticas import Gramatica, Producciones
from Automatas import Automatas, Transiciones
from graphviz import Graph
from webbrowser import open_new_tab
import os

''' PANTALLA PRINCIPAL DE LA APLCIACION'''


class PantallaPrincipal():
    def __init__(self):

        self.lista_nombres_Gramatica=[]
        self.lista_nombres_Automatas=[]
        self.lista_Gramaticas=[]
        self.lista_Automatas=[]
        self.lista_no_terminales=[]
        #self.moduloMain = ModuloPrincipal()
        self.ventana = Tk()
        self.ventana.resizable(True, False)  # Redimensionar la ventana
        self.ventana.title('Pantalla Principal')  # Titulo de la ventana
        self.ventana.geometry('1100x700')  # Tamaño de la ventana
        self.Centrar(self.ventana, 1000, 700)  # Centrar la ventana
        self.ventana.config(bg='#172a39')
        self.Ventana()  # Llamar a la ventana
        #self.a= ModuloPrincipal()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()  # Altura de la pantalla
        ancho_pantalla = r.winfo_screenwidth()  # Ancho de la pantalla

        x = (ancho_pantalla // 2) - (ancho // 2)  # Posicion de la ventana
        y = (altura_pantalla // 2) - (alto // 2)  # Posicion de la ventana
        r.geometry(f'+{x}+{y}')  # Posicion de la ventana

    def Ventana(self):
        # Se coloca sobre la ventana
        self.frame = Frame(height=1000, width=800)
        self.frame.config(bg='#3d5568')
        self.frame.pack(padx=40, pady=40, fill=tk.X)

        Label(self.frame, text="Lenguajes Formales y de Programación ", font=(
            'Times New Roman', 40), fg='#ffffff', bg='#3d5568', width=40).place(x=-100, y=10)
        Label(self.frame, text="Sección: N", font=('Times New Roman', 20),
              fg='#ffffff', bg='#3d5568', width=40).place(x=-140, y=125)
        Label(self.frame, text="Carné: 202010844 ", font=('Times New Roman',
              20), fg='#ffffff', bg='#3d5568', width=40).place(x=-100, y=200)
        Label(self.frame, text="Kevin José de la Cruz Girón ", font=(
            'Times New Roman', 20), fg='#ffffff', bg='#3d5568', width=40).place(x=-50, y=275)

        Button(self.frame, text="Módulo gramática libre de contexto", command=self.modGramatica, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=30).place(x=200, y=350)

        Button(self.frame, text="Módulo autómatas de pila", command=self.modAutomata, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=30).place(x=200, y=420)
        
        Button(self.frame, text="Salir", command=self.frame.quit, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=15).place(x=300, y=500)

        self.frame.mainloop()

    def modGramatica(self):
        ventana = tk.Tk()
        ventana.geometry('1000x600')
        ventana.config(bg='#172a39')
        ventana.title("Ventana Gramática")
        ventana.resizable(True, False)

        


        Label(ventana, text="Módulo Gramática ", font=(
            'Times New Roman', 40), fg='#ffffff', bg='#3d5568', width=40).grid(row=0,column=0)

        Button(ventana, text="Carga Archivos", command=self.ventanaArchivo, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=20).grid(row=2,column=0,pady=40)
        
        Button(ventana, text="Mostrar información General", command=self.mostrarInformacion, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=40).grid(row=3,column=0,pady=30)

        Button(ventana, text="Árbol de derivación", command=self.Arbol_Gramatica, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=20).grid(row=4,column=0,pady=30)
        
        Button(ventana, text="Regresar", command=ventana.destroy, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=15).grid(row=5,column=0,pady=30)
        
    
    def mostrarInformacion(self):
        ventana = tk.Tk()

        ventana.geometry("400x200")
        ventana.title("Ventana de Mostrar información.")
        ventana.config(bg="#172a39")
        ventana.resizable(False, False)

        etiquetaCarga = tk.Label(ventana, text="Seleccionar la gramática a mostrar", font=(
            "Agency FB", 18), bg="#3d5568", foreground="white").grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        options_list = []

        # reccorer lista_automatas para obtener los nombres de los automatas y mostrarlos en el combobox
        for gramatica in self.lista_Gramaticas:
            options_list.append(gramatica.nombre)

        
        value_inside = tk.StringVar(ventana)
        value_inside.set("Selecciona una gramática")

        question_menu = tk.OptionMenu(ventana, value_inside, *options_list)
        question_menu.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # button to get the option selected
        # from the optionmenu widget
        btnAgrega = tk.Button(
            ventana, text="Mostrar Información", font=('Times New Roman', 15), foreground='#000000',
            command=lambda:mostrarInfo(value_inside.get()))
        btnAgrega.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        def mostrarInfo(nombre_):
            ventana.destroy()

            ventanamuestra = tk.Tk()
            ventanamuestra.geometry("500x450")
            ventanamuestra.title("Ventana de Mostrar información.")
            ventanamuestra.config(bg="#172a39")
            ventanamuestra.resizable(True, False)

            gramatica_=""
            gramaticaBuscada=None
            for list in self.lista_Gramaticas:
                if list.nombre == nombre_:
                    gramaticaBuscada=list

            gramatica_=""
            gramatica_+= f'Nombre: {gramaticaBuscada.nombre}\n'

            noTerminales_=""
            for list__ in gramaticaBuscada.no_terminales:
                noTerminales_+=f'{list__},'
            gramatica_ += f'No Terminales: {noTerminales_}\n'
            
            terminales_ = ''
            for t in range(0,len(gramaticaBuscada.terminales)):
                if t+1 == len(gramaticaBuscada.terminales):
                    terminales_ += f'{gramaticaBuscada.terminales[t]}'
                else:
                    terminales_ += f'{gramaticaBuscada.terminales[t]},'
            gramatica_ += f'Terminales: {terminales_}\n'
            gramatica_ += f'No terminal inicial: {gramaticaBuscada.nti}\n'
            
            gramatica_ += f'Producciones:\n'

            anterior = ''
            for produccion in gramaticaBuscada.producciones:
                cadenaP = ''
                if anterior != produccion.origen:
                    cadenaP += f'{produccion.origen}>'
                    for ex in produccion.destinos:
                        cadenaP += f'{ex} '
                    gramatica_ += f'{cadenaP}\n'
                    anterior = produccion.origen
                elif anterior == produccion.origen:
                    cadenaP += f'   |'
                    for ex in produccion.destinos:
                        cadenaP += f'{ex} '
                    gramatica_ += f'{cadenaP}\n'
                    

            T=tk.Text(ventanamuestra, height=20, width=60)
            T.grid(row=0,column=1,padx=5, pady=5)
            T.insert(tk.END, gramatica_)

            Button(ventanamuestra, text="Cerrar", command=ventanamuestra.destroy, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=15).grid(row=1,column=1,pady=30)
                    

    def Arbol_Gramatica(self):
        ventana = tk.Tk()

        ventana.geometry("400x200")
        ventana.title("Ventana de derivación.")
        ventana.config(bg="#172a39")
        ventana.resizable(False, False)

        etiquetaCarga = tk.Label(ventana, text="Seleccionar la gramática a graficar", font=(
            "Agency FB", 18), bg="#3d5568", foreground="white").grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        options_list = []

        # reccorer lista_automatas para obtener los nombres de los automatas y mostrarlos en el combobox
        for gramatica in self.lista_Gramaticas:
            options_list.append(gramatica.nombre)

        
        value_inside = tk.StringVar(ventana)
        value_inside.set("Selecciona una gramática")

        question_menu = tk.OptionMenu(ventana, value_inside, *options_list)
        question_menu.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # button to get the option selected
        # from the optionmenu widget
        btnAgrega = tk.Button(
            ventana, text="Generar Árbol", font=('Times New Roman', 15), foreground='#000000',
            command=lambda:generarArbol(value_inside.get()))
        btnAgrega.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        def generarArbol(nombre):
            
            for names in self.lista_nombres_Gramatica:
                if nombre == names:
                    resp = self.lista_nombres_Gramatica.index(names)
                    resp = resp+1

            z = False
            while not z:
                    y = 1
                    for x in self.lista_nombres_Gramatica:
                        y+=1
                    if resp in self.lista_nombres_Gramatica:
                        j = self.lista_nombres_Gramatica(resp)
                        resp = j+1
                    if resp !='0' and int(resp)>0:

                        dot = Graph(name='GramaticaLC', encoding='utf-8', format='png', filename='GramaticasLC')

                        dot.attr(rankdir='TB', layout='dot', shape='none')

                        numero = -1
                        listaP = []
                        indice = 0
                        aux = 0
                        lista_Nodos = []
                        r_2 = int(resp)-1
                        for nodo in self.lista_Gramaticas[r_2].producciones:
                            aux = 0
                            if lista_Nodos[:] != []:
                                for x in lista_Nodos:
                                    if nodo.origen == x:
                                        indice = aux
                                    aux+=1
                            else:
                                numero+=1
                                dot.node(name='nodo'+str(numero), label=nodo.origen, shape='none')
                                lista_Nodos.append(nodo.origen)
                            
                            for y in nodo.destinos:
                                numero +=1
                                dot.node(name='nodo'+str(numero), label=y, shape='none')
                                listaP.append(numero)
                                lista_Nodos.append(y)
                            for z in listaP:
                                dot.edge('nodo'+str(indice), 'nodo'+str(z))
                            listaP = []
                            aux = 0
                        MessageBox.showinfo(message="Se esta abriendo el archivo")
                        dot.render('GramaticasLC/'+self.lista_Gramaticas[r_2].nombre, format='png' ,view=True)
                        
                    elif int(resp) <0:
                        print('\nERROR: Selecciona una opcion valida\n')
                        #input(continuar)
                    else:
                        z = True
                
            ventana.destroy()
        

    def modAutomata(self):
        ventana = tk.Tk()
        ventana.geometry('1000x600')
        ventana.config(bg='#172a39')
        ventana.title("Ventana Autómatas")
        ventana.resizable(True, False)

        Label(ventana, text="Módulo Autómata ", font=(
            'Times New Roman', 40), fg='#ffffff', bg='#3d5568', width=40).grid(row=0,column=0)

        Button(ventana, text="Carga Archivos", command=self.ventanaArchivo, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=20).grid(row=2,column=0,pady=40)
        
        Button(ventana, text="Mostrar información de Autómata", command=self.mostrarInfoAuto, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=40).grid(row=3,column=0,pady=30)

        Button(ventana, text="Validar una cadena", command=self.validarCadena, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=20).grid(row=4,column=0,pady=30)
        
        Button(ventana, text="Ruta de validación", command="", font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=20).grid(row=5,column=0,pady=30)
        
        """Button(ventana, text="Recorrido paso a paso", command="", font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=20).grid(row=5,column=1,pady=30)
        
        Button(ventana, text="Validar cadena en una pasada", command="", font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=30).grid(row=5,column=0,pady=30)
        """
        Button(ventana, text="Regresar", command=ventana.destroy, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=15).grid(row=6,column=0,pady=30)
        
    def mostrarInfoAuto(self):
        ventana = tk.Tk()

        ventana.geometry("400x200")
        ventana.title("Ventana de Mostrar Autómata.")
        ventana.config(bg="#172a39")
        ventana.resizable(False, False)

        etiquetaCarga = tk.Label(ventana, text="Seleccionar el autómata a mostrar", font=(
            "Agency FB", 18), bg="#3d5568", foreground="white").grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        options_list = []

        # reccorer lista_automatas para obtener los nombres de los automatas y mostrarlos en el combobox
        for automata in self.lista_Automatas:
            options_list.append(automata.nombre)

        
        value_inside = tk.StringVar(ventana)
        value_inside.set("Selecciona un Autómata")

        question_menu = tk.OptionMenu(ventana, value_inside, *options_list)
        question_menu.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # button to get the option selected
        # from the optionmenu widget
        btnAgrega = tk.Button(
            ventana, text="Generar PDF", font=('Times New Roman', 15), foreground='#000000',
            command=lambda:mostrarInfo(value_inside.get()))
        btnAgrega.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        print("Mostrar información de Autómata")


        def mostrarInfo(nombre):
            ventana.destroy()
            busqueda=None
            for automata in self.lista_Automatas:
                if automata.nombre == nombre:
                    busqueda = automata
            
            nombre = busqueda.nombre
            alfabeto = busqueda.alfabeto
            simbolosPila = busqueda.simbolosPila
            estados = busqueda.estados
            estadoInicial = busqueda.estadoInicial
            estadosAceptacion = busqueda.estadosAceptacion
            transiciones = busqueda.transiciones

            cd_alfabeto = ""
            for q in range(0,len(alfabeto)):
                if q+1 == len(alfabeto):
                    cd_alfabeto += f'{alfabeto[q]}'
                else:
                    cd_alfabeto += f'{alfabeto[q]},'
            
            cadena_simbolosP = ''
            for w in range(0,len(simbolosPila)):
                if w+1 == len(simbolosPila):
                    cadena_simbolosP += f'{simbolosPila[w]}'
                else:
                    cadena_simbolosP += f'{simbolosPila[w]},'
            
            cadena_estados = ''
            for e in range(0,len(estados)):
                if e+1 == len(estados):
                    cadena_estados += f'{estados[e]}'
                else:
                    cadena_estados += f'{estados[e]},'
            
            cadena_estadosAceptacion = ''
            for r in range(0,len(estadosAceptacion)):
                if r+1 == len(estadosAceptacion):
                    cadena_estadosAceptacion += f'{estadosAceptacion[r]}'
                else:
                    cadena_estadosAceptacion += f'{estadosAceptacion[r]},'
            
            cadena = 'digraph grafo_afd { \r'
            cadena += '     fontname="Helvetica,Arial,sans-serif"\r'
            cadena += '     edge [fontname="Helvetica,Arial,sans-serif"]\r'
            cadena += '	    rankdir=LR;\r'
            for e_aceptacion in busqueda.estadosAceptacion:
                cadena += f'	    {e_aceptacion} [shape=doublecircle]\r'

            
            cadena += '     	node [shape = circle];\r'
            for transicion in transiciones:
                simboloEntrada_ = ''
                simboloextraPila_ = ''
                simboloinsertaPila_ = ''
                if transicion.simboloEntrada == '$':
                    simboloEntrada_ = 'λ'
                else:
                    simboloEntrada_ = transicion.simboloEntrada

                if transicion.simboloextraPila == '$':
                    simboloextraPila_ = 'λ'
                else:
                    simboloextraPila_ = transicion.simboloextraPila

                if transicion.simboloinsertaPila == '$':
                    simboloinsertaPila_ = 'λ'
                else:
                    simboloinsertaPila_ = transicion.simboloinsertaPila

                cadena += f'     {transicion.estadoOrigen} -> {transicion.estadoDestino} [label = "{simboloEntrada_},{simboloextraPila_};{simboloinsertaPila_}"];\r'

            # espacio para el cuadro
            nombre_sin_espacio = (busqueda.nombre).strip()
            cadena += f'     {nombre_sin_espacio} [\r'
            cadena += f'            fillcolor="#ff880022"\r'
            cadena += f'            label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="18"> \r'
            cadena += f'            <tr> <td> <b>Nombre: {busqueda.nombre}</b> </td> </tr> \r'
            cadena += f'            <tr> <td> Alfabeto: {cd_alfabeto}</td> </tr>\r'
            cadena += f'            <tr> <td> Alfabeto de pila: {cadena_simbolosP}</td> </tr>\r'
            cadena += f'            <tr> <td> Estados: {cadena_estados}</td> </tr> \r'
            cadena += f'            <tr> <td> Estado inicial: {estadoInicial}</td> </tr> \r'
            cadena += f'            <tr> <td> Estado aceptacion: {estadosAceptacion}</td> </tr> \r'
            cadena += f'            <tr> <td align="left"> \r'
            cadena += f'            <br align="left"/>\r'
            cadena += f'     Transiciones:<br align="left"/>\r'
            for t in transiciones:
                simboloEntrada__ = ''
                simboloextraPila__ = ''
                simboloinsertaPila__ = ''
                if t.simboloEntrada == '$':
                    simboloEntrada__ = 'λ'
                else:
                    simboloEntrada__ = t.simboloEntrada

                if t.simboloextraPila == '$':
                    simboloextraPila__ = 'λ'
                else:
                    simboloextraPila__ = t.simboloextraPila

                if t.simboloinsertaPila == '$':
                    simboloinsertaPila__ = 'λ'
                else:
                    simboloinsertaPila__ = t.simboloinsertaPila
                cadena += f'     {t.estadoOrigen},{simboloEntrada__},{simboloextraPila__};{t.estadoDestino},{simboloinsertaPila__} <br align="left"/>\r'

            cadena += f'            <br align="left"/>\r'
            cadena += f'            </td> </tr>\r'

            cadena += f'            </table>> \r'
            cadena += f'            shape=plain \r'
            cadena += f']\r'

            cadena += "}"

            file = open(f"Automatas/grafo_{nombre_sin_espacio}.dot", "w+", encoding="utf-8")
            file.write(cadena)
            file.close()
            os.system(f'dot -Tpdf Automatas/grafo_{nombre_sin_espacio}.dot -o Automatas/grafo_{nombre_sin_espacio}.pdf')

            MessageBox.showinfo('GENERACION CORRECTA','EL DOCUMENTO SE CREO',detail='SE CREO UN PDF CON EL Automata SELECCIONADO, ESTA EN LA CARPETA Automatas')
            open_new_tab(f"Automatas\grafo_{nombre_sin_espacio}.pdf")

    def validarCadena(self):
        if self.lista_Automatas == []:
            MessageBox.showwarning("Alerta", "No hay automatas cargados")
        else:
            ventanaCadena = tk.Tk()
            ventanaCadena.title("Validar cadena")
            ventanaCadena.geometry("500x200")
            ventanaCadena.resizable(0,0)
            ventanaCadena.config(bg="#172a39")

            lbl_automata = tk.Label(ventanaCadena, text="Seleccione el automata", bg="#172a39", fg="white", font=("Arial", 12))
            lbl_automata.grid(row=0, column=0, padx=10, pady=10)

            cbx_automata = ttk.Combobox(ventanaCadena, values=self.lista_nombres_Automatas, state="readonly")
            cbx_automata.grid(row=0, column=1, padx=10, pady=10)
    
            lbl_cadena = tk.Label(ventanaCadena, text="Ingrese la cadena", bg="#2B2B2B", fg="white")
            lbl_cadena.grid(row=1, column=0, padx=10, pady=10)

            txt_cadena = tk.Entry(ventanaCadena)
            txt_cadena.grid(row=1, column=1, padx=10, pady=10)

            

        
            def validar():
                entrada = txt_cadena.get()
                if cbx_automata.get() == "":
                    MessageBox.showwarning("Alerta", "Seleccione un automata")
                elif entrada == "":
                    MessageBox.showwarning("Alerta", "Ingrese una cadena")
                else:
                    for automata in self.lista_Automatas:
                        if automata.nombre == cbx_automata.get():
                            if validarCadena(entrada):
                                MessageBox.showinfo("Cadena aceptada", "La cadena fue aceptada")
                            else:
                                MessageBox.showinfo("Cadena no aceptada", "La cadena no fue aceptada")

            btn_validar = tk.Button(ventanaCadena, text="Validar", command=validar)
            btn_validar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

            def validarCadena(nombreADPL):
                
                print(nombreADPL)
    
    def ventanaArchivo(self):
        ventanaCarga = tk.Tk()

        def almacenar(contenido):
            
            x = 1
            lista_producciones = []
            lista_terminales = []
            lista_no_terminales = []
            lctxt = False
            for file in contenido:
                file = file.rstrip('\n')
                if x==1:
                    nombre=file
                    if (nombre in self.lista_nombres_Gramatica):
                        MessageBox.showwarning("Alerta", "La gramática ***{nombre}***sera saltada debido a que ya existe")
                        x = '%'
                    else:
                        self.lista_nombres_Gramatica.append(nombre)

                if x==2:
                    file = file.replace(' ','')
                    le = file.split(",")
                    for l in le:
                        lista_no_terminales.append(l)

                if x==3:
                    la = file.split(',')
                    la.sort()
                    for listae in lista_no_terminales:
                        for listaa in lista_terminales:
                            if listaa == listae:
                                MessageBox.showwarning("Alerta", "No fue posible crear la gramática  debido a que el alfabeto de entrada contiene simbolos no terminales")
                                self.lista_nombres_Gramatica.remove(nombre)
                                x = '%'
                    for list_ in la:   
                        lista_terminales.append(list_)

                if x==4:
                    einic = file
                    recorrer = False
                    for ee in lista_no_terminales:
                        if einic == ee:
                            recorrer = True
                    if recorrer == False:
                        MessageBox.showwarning("Alerta", "No fue posible crear la gramática debido a que el estado inicial no es un no terminal")
                        self.lista_nombres_Gramatica.remove(nombre)
                        x = '%'
                    else:
                        einicial = False

                if x != '%':
                    if x>=5 and file != '%':
                        files = file.split('>')
                        files2 = files[1].split()
                        if len(files2) >= 3:
                            lctxt = True

                        if ((files[0] in lista_no_terminales) and (files[1] in lista_no_terminales)):
                            lctxt = True
                        
                        if (files[0] in lista_terminales) and (files[1] in lista_terminales):
                            lctxt = True

                        if len(files2) == 1 and files2[0] in lista_no_terminales:
                            lctxt = True
                        lista_producciones.append(Producciones(files[0], files2))

                if file == '%' and x!="%":
                    if lctxt == True:
                        self.lista_Gramaticas.append(Gramatica(nombre, lista_no_terminales, lista_terminales, einic, lista_producciones))
                        lista_producciones = []
                        lista_terminales = []
                        lista_no_terminales = []
                        x = 0
                        lctxt = False
                    else:
                        MessageBox.showwarning("Alerta", "No fue posible crear la gramatica debido a que la gramatica no es libre de contexto")
                        self.lista_nombres_Gramatica.remove(nombre)
                        lista_producciones = []
                        lista_terminales = []
                        lista_no_terminales = []
                        x = 0

                if file == '%':
                    lista_producciones = []
                    lista_terminales = []
                    lista_no_terminales = []
                    x = 0

                if x!='%':
                    x+=1

            MessageBox.showinfo("Información", "Se han cargado las gramáticas correctamente")
            ventanaCarga.destroy()

        def almacenarAutomata(contenido):
            
            x = 1
            lista_transiciones = []
            lista_alfabeto = []
            lista_simbolosPila = []
            lista_estados = []
            lctxt = False
            for file in contenido:
                file = file.rstrip('\n')
                if x==1:
                    nombre=file
                    if (nombre in self.lista_nombres_Automatas):
                        MessageBox.showwarning("Alerta", "El automata ***{nombre}***sera saltado debido a que ya existe")
                        x = '%'
                    else:
                        self.lista_nombres_Automatas.append(nombre)
                        

                if x==2:
                    file = file.replace(' ','')
                    le = file.split(",")
                    for l in le:
                        lista_alfabeto.append(l)

                if x==3:
                    la = file.split(',')
                    for listae in lista_alfabeto:
                        for listaa in lista_simbolosPila:
                            if listaa == listae:
                                MessageBox.showwarning("Alerta", "No fue posible crear el automata  debido a que el alfabeto de entrada contiene simbolos no terminales")
                                self.lista_nombres_Automatas.remove(nombre)
                                x = '%'
                    for list_ in la:   
                        lista_simbolosPila.append(list_)

                if x==4:
                    file = file.replace(' ','')
                    le = file.split(",")
                    for l in le:
                        lista_estados.append(l)
                
                if x==5:
                    einic = file
                    recorrer = False
                    for ee in lista_estados:
                        if einic == ee:
                            recorrer = True
                    if recorrer == False:
                        MessageBox.showwarning("Alerta", "No fue posible crear el automata debido a que el estado inicial no es un no terminal")
                        self.lista_nombres_Automata.remove(nombre)
                        
                    else:
                        einicial = False

                if x==6:
                    eacept = file
                    recorrer = False
                    for ee in lista_estados:
                        if eacept == ee:
                            recorrer = True
                    if recorrer == False:
                        MessageBox.showwarning("Alerta", "No fue posible crear el automata debido a que el estado inicial no es un estado definido")
                        self.lista_nombres_Automata.remove(nombre)
                        x = '%'
                    else:
                        einicial = False

                if x != '%':
                    if x>=7 and file != '%':
                        files = file.split(';')
                        files2 = files[0].split(",")
                        files3 = files[1].split(",")
                        if len(files2) >= 3:
                            lctxt = True

                        if ((files2[0] in lista_estados) and (files3[0] in lista_alfabeto)):
                            lctxt = True
                        
                        
                        lista_transiciones.append(Transiciones(files2[0], files2[1], files2[2], files3[0], files3[1]))

                if file == '%' and x!="%":
                    if lctxt == True:
                        self.lista_Automatas.append(Automatas(nombre, lista_alfabeto, lista_simbolosPila, lista_estados, einic, eacept, lista_transiciones))
                        lista_estados = []
                        lista_alfabeto = []
                        lista_simbolosPila = []
                        lista_transiciones = []
                        x = 0
                        lctxt = False
                    else:
                        MessageBox.showwarning("Alerta", "No fue posible crear el Autómata debido a que el autómata no es de pila")
                        self.lista_nombres_Automatas.remove(nombre)
                        lista_estados = []
                        lista_alfabeto = []
                        lista_simbolosPila = []
                        lista_transiciones = []
                        x = 0

                if file == '%':
                    lista_estados = []
                    lista_alfabeto = []
                    lista_simbolosPila = []
                    lista_transiciones = []
                    x = 0

                if x!='%':
                    x+=1

            MessageBox.showinfo("Información", "Se han cargado los autómatas correctamente")
            ventanaCarga.destroy()

        def seleccionarArchivo():
            file = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("glc files", "*.glc"), ("all files", "*.ap")))
            if file is None:
                print("No has seleccioado ningun archivo.".center(50, "!"))
                return None
            else:
                extension = file[-3:]
                if extension == "glc":
                    with open(file, 'r', encoding='utf-8') as infile:
                        almacenar(infile)

                elif extension == ".ap":
                    with open(file, 'r', encoding='utf-8') as infile:
                        almacenarAutomata(infile)

                    #curso = Curso(item[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6])
                    # ListaEnlazada.insertar(curso)

        
        # ventana de carga
        ventanaCarga.geometry("400x300")
        ventanaCarga.title("Ventana de Carga")
        ventanaCarga.config(bg="#172a39")
        ventanaCarga.resizable(False, False)

        etiquetaCarga = tk.Label(ventanaCarga, text="Seleccionar el archivo a leer", font=(
            "Agency FB", 18), bg="#3d5568", foreground="white").place(x=100, y=40)

        botonElegir = ttk.Button(
            ventanaCarga, text="Carga de Archivos", command=seleccionarArchivo)
        botonElegir.place(x=120, y=150, width=190, height=60)
        
    


PantallaPrincipal()
