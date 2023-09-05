from tkinter import *
from tkinter import messagebox

#-------------------limpiar ventanas
def limpiar():
    pass
    lista_impares.delete(0, 'end')
    lista_pares.delete(0, 'end')
    lista_primos.delete(0, 'end')

#-------------------validación de numero
def validar():
    
    try:
        numero = int(entrynumero1.get())
        contador = 0

#-------------------validación de numero primo
        for n in range(2, numero):
            if numero % n == 0:
                contador += 1
        if contador==0:
            lista_primos.insert(0, numero)
        else:
            pass
#-------------------validación de numero par o impar
        if numero%2==0:
            lista_pares.insert(0, numero)
        else:
            lista_impares.insert(0, numero)

        #messagebox.showinfo('Info', f'El numero ingresado es {numero}')
               
    except Exception as e:
        messagebox.showinfo('Error',f'Se presentó un error de tipo {e}') 

# ventana
mainroot = Tk()
mainroot.title("listbox")
mainroot.geometry('400x450')





labelnumero1 = Label(mainroot, text = 'INGRESA UN NÚMERO')
labelnumero1.place(x = 10, y = 60, width = 180, height = 30)

entrynumero1 = Entry(mainroot)
entrynumero1.place(x = 210, y = 60, width = 180, height = 30)


calcular = Button(mainroot, text ='Validar', command = validar)
calcular.place(x = 140, y = 100, width = 120, height = 30)

titulo_listbox_primos = Label(mainroot, text = 'Primo')
titulo_listbox_primos.place(x = 40, y = 145, width = 60, height = 20)

lista_primos = Listbox(mainroot)
lista_primos.place(x = 20, y = 170, width = 100, height = 200)

titulo_listbox_pares = Label(mainroot, text = 'Par')
titulo_listbox_pares.place(x = 170, y = 145, width = 60, height = 20)

lista_pares = Listbox(mainroot)
lista_pares.place(x = 150, y = 170, width = 100, height = 200)

titulo_listbox_impares = Label(mainroot, text = 'Impar')
titulo_listbox_impares.place(x = 290, y = 145, width = 60, height = 20)

lista_impares = Listbox(mainroot)
lista_impares.place(x = 270, y = 170, width = 100, height = 200)

borrar = Button(mainroot, text ='Limpiar', command = limpiar)
borrar.place(x = 140, y = 400, width = 120, height = 30)


mainroot.mainloop()