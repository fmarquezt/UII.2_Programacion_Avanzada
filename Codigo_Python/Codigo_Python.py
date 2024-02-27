"""
Programa Python implementado para comunicacion serial.
Evidencia UII.2
IMEC91N
-Fernando Marquez
-Dilan Rojas
-Oscar Vazquez
-Jason Robledo
-Aaron Garcia
"""




import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
import serial ,time

#Profesor Porfavor ingrese aqui el COM a utilizar
Puerto = 'COM9'



app = tk.Tk()
app.title("Serial Comunicacion")
app.geometry("250x150")

fig = plt.figure()
ax = fig.add_subplot(1,1,1)



Comunicacion = serial.Serial(port=Puerto,baudrate=9600)
time.sleep(2)

xs = [0]
ys = [1]



#Funcion que permite la animacion del grafico
def animar(i,xs,ys):
    valor= Comunicacion.readline()
    ValorString = str(valor,'UTF-8')
    ValorFloat = float(ValorString.strip())

    y = ValorFloat
    x = xs[-1] + 1
    
    xs.append(x)
    ys.append(y)

    ax.clear()
    ax.plot(xs,ys)

ani = animation.FuncAnimation(fig,animar, fargs=(xs,ys), interval = 50)






#Funcion que escribe Serialmente un valor.
def Accion(boton,accion):
    if boton== 1 and accion == "ON":
        Comunicacion.write(b'1')
    elif boton== 1 and accion == "OFF":
        Comunicacion.write(b'2')
    elif boton== 2 and accion == "ON":
        Comunicacion.write(b'A')
    elif boton== 2 and accion == "OFF":
        Comunicacion.write(b'B')
        
        
    
    
#Frame 1, para control LED1
Frame1 = tk.Frame(app)
Frame1.pack(side='top',pady=10)

Label1 = tk.Label(Frame1,text="Control Led 1")
Label1.pack()

Boton_on1 = tk.Button(Frame1,text = 'ON',bg='green',command = lambda: Accion(1,"ON"))
Boton_on1.pack(side='left',padx=10)

Boton_off1 = tk.Button(Frame1,text = 'OFF',bg= 'red', command = lambda: Accion(1,"OFF"))
Boton_off1.pack(side='left',padx=10)

#Frame 2, para control LED2
Frame2 = tk.Frame(app)
Frame2.pack(side='top',pady=10)

Label2 = tk.Label(Frame2,text="Control Led 1")
Label2.pack()

Boton_on2 = tk.Button(Frame2,text = 'ON',command = lambda: Accion(2,"ON"))
Boton_on2.pack(side='left',padx=10)

Boton_off2 = tk.Button(Frame2,text = 'OFF',command = lambda: Accion(2,"OFF"))
Boton_off2.pack(side='left',padx=10)


plt.show()

app.mainloop()


