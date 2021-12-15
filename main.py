import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Exposición place()")
ventana.geometry('800x500')
ventana.resizable(False, False)
 

principal_frame = tk.Frame(ventana)
principal_frame.config(bg='blue', bd=1)
principal_frame.place(width= 800, height=500)

frame1 = tk.Frame(principal_frame)
frame1.config(bg='cyan')
frame1.config(bd=10)
frame1.config(cursor="plus")
frame1.config(relief="ridge")
frame1.place(x=10, y=10, width=780, height=90)

title = tk.Label(frame1, text='Ejemplo Frames y Place')
title.config(fg='red', bg='cyan', font=("Times",15))
title.place(x=250, y= 20)



frame2 = tk.Frame(principal_frame)
frame2.config(bg='dark green')
frame2.config(bd=1)
frame2.config(cursor="pirate")
frame2.config(relief="ridge")
frame2.place(x=10, y=110, width=365, height=380)


frame3 = tk.Frame(frame2,bg='green',bd=5,cursor="arrow",relief="ridge")
frame3.place(x=10, y=10, relheight=0.45,width=345)

rbutton1 = tk.Radiobutton(frame3, text="Opción 1")
rbutton1.place(relx=0.35, y=5)
rbutton2 = tk.Radiobutton(frame3, text="Opción 2")
rbutton2.place(relx=0.35, y=65)
rbutton3 = tk.Radiobutton(frame3, text="Opción 3")
rbutton3.place(relx=0.35, y=125)


frame4 = tk.Frame(frame2, bg='green', bd=5, cursor="plus", relief="ridge")
frame4.place(x=10, y=185, relheight=0.50, width=345)

boton1 = tk.Button(frame4, text="Ganaste!")
boton1.config(bg='light green', fg='black', cursor="question_arrow")
boton1.place(height=50, relwidth=0.5, relx=0.25, rely=0.35)



frame5 = tk.Frame(principal_frame,bg='light gray',bd=1,cursor="pirate",relief="ridge")
frame5.place(x=385, y=110, width=405, height=380)

boton = tk.Button(frame5, text="Hola!")
boton.config(bg='gray', fg='black', cursor="question_arrow")
boton.place(height=50, relwidth=0.5, relx=0.25, y=10)

leon_imagen = tk.PhotoImage(file = r"leon.png")
imagen = leon_imagen.subsample(2, 2)
label_image = tk.Label(frame5, image = imagen)
label_image.config(bg='light gray')
label_image.place(relx=0.27, y=100)

ventana.mainloop()