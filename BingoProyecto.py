import random,os
from tkinter import *
from PIL import ImageTk, Image
import time

os.system ("cls") 

print('''
                                                     ____    _____   ______   _   _  __      __  ______   _   _   _____   _____     ____                 _      
                                                    |  _ \  |_   _| |  ____| | \ | | \ \    / / |  ____| | \ | | |_   _| |  __ \   / __ \        /\     | |     
                                                    | |_) |   | |   | |__    |  \| |  \ \  / /  | |__    |  \| |   | |   | |  | | | |  | |      /  \    | |     
                                                    |  _ <    | |   |  __|   | . ` |   \ \/ /   |  __|   | . ` |   | |   | |  | | | |  | |     / /\ \   | |     
                                                    | |_) |  _| |_  | |____  | |\  |    \  /    | |____  | |\  |  _| |_  | |__| | | |__| |    / ____ \  | |____ 
                                                    |____/  |_____| |______| |_| \_|     \/     |______| |_| \_| |_____| |_____/   \____/    /_/    \_\ |______|
                                                                                                                                    
                                                                            
                                                        .----------------.  .----------------.  .-----------------. .----------------.  .----------------. 
                                                        | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
                                                        | |   ______     | || |     _____    | || | ____  _____  | || |    ______    | || |     ____     | |
                                                        | |  |_   _ \    | || |    |_   _|   | || ||_   \|_   _| | || |  .' ___  |   | || |   .'    `.   | |
                                                        | |    | |_) |   | || |      | |     | || |  |   \ | |   | || | / .'   \_|   | || |  /  .--.  \  | |
                                                        | |    |  __'.   | || |      | |     | || |  | |\ \| |   | || | | |    ____  | || |  | |    | |  | |
                                                        | |   _| |__) |  | || |     _| |_    | || | _| |_\   |_  | || | \ `.___]  _| | || |  \  `--'  /  | |
                                                        | |  |_______/   | || |    |_____|   | || ||_____|\____| | || |  `._____.'   | || |   `.____.'   | |
                                                        | |              | || |              | || |              | || |              | || |              | |
                                                        | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
                                                        '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
''')

time.sleep(2)
os.system ("cls") 

num_elegidos=[]
numeros=[]
for i in range(1,101):
    numeros.append(i)
    
def numeros_random():
    global c
    c=[]
    c=random.sample(numeros,1)
    numeros.remove(c[0])
    text1.delete('1.0',END)
    text1.insert(INSERT,c[0])
       
def elim_nums():
    try:
        for i in range(len(listo)):
            if listo[i]==c[0]:
                text1.delete('1.0',END)           
                if str(lab1.cget("text"))==str(c[0]):
                    lab1.config(bg="red")
                elif str(lab2.cget("text"))==str(c[0]):
                    lab2.config(bg="red")
                elif str(lab3.cget("text"))==str(c[0]):
                    lab3.config(bg="red")
                elif str(lab4.cget("text"))==str(c[0]):
                    lab4.config(bg="red")  
                elif str(lab5.cget("text"))==str(c[0]):
                    lab5.config(bg="red")  
                elif str(lab6.cget("text"))==str(c[0]):
                    lab6.config(bg="red") 
                elif str(lab7.cget("text"))==str(c[0]):
                    lab7.config(bg="red") 
                elif str(lab8.cget("text"))==str(c[0]):
                    lab8.config(bg="red")
                elif str(lab9.cget("text"))==str(c[0]):
                    lab9.config(bg="red")
                elif str(lab10.cget("text"))==str(c[0]):
                    lab10.config(bg="red")
                elif str(lab11.cget("text"))==str(c[0]):
                    lab11.config(bg="red")
                elif str(lab12.cget("text"))==str(c[0]):
                    lab12.config(bg="red")  
                elif str(lab13.cget("text"))==str(c[0]):
                    lab13.config(bg="red")  
                elif str(lab14.cget("text"))==str(c[0]):
                    lab14.config(bg="red") 
                elif str(lab15.cget("text"))==str(c[0]):
                    lab15.config(bg="red") 
                elif str(lab16.cget("text"))==str(c[0]):
                    lab16.config(bg="red")
                elif str(lab17.cget("text"))==str(c[0]):
                    lab17.config(bg="red")
                elif str(lab18.cget("text"))==str(c[0]):
                    lab18.config(bg="red")  
                elif str(lab19.cget("text"))==str(c[0]):
                    lab19.config(bg="red") 
                elif str(lab20.cget("text"))==str(c[0]):
                    lab20.config(bg="red") 
                elif str(lab21.cget("text"))==str(c[0]):
                    lab21.config(bg="red")
                elif str(lab22.cget("text"))==str(c[0]):
                    lab22.config(bg="red")
                elif str(lab23.cget("text"))==str(c[0]):
                    lab23.config(bg="red")
                elif str(lab24.cget("text"))==str(c[0]):
                    lab24.config(bg="red")
                elif str(lab25.cget("text"))==str(c[0]):
                    lab25.config(bg="red")          
    except Exception:
        text1.delete('1.0',END)
        text1.insert(INSERT,"Por favor, introduce un número antes")        
    ventana.update()   
         
def elegir_num():
    listo=[]
    while (len(listo)<=25):
        k=random.choice(range(1,101))
        if k not in listo:listo.append(k)
    return listo     

if __name__=='__main__':
    listo=elegir_num()
    
    menu_carga=Tk()
    menu_carga.title('Cargando...')
    carga=Label(menu_carga)
    # menu_carga.geometry("1920x1080")
    menu_carga.attributes('-fullscreen', True)
    menu_carga.config(bg="black")
    img = ImageTk.PhotoImage(Image.open("imagen.png"))
    panel = Label(menu_carga, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    carga.pack()
    menu=Label(menu_carga)
    menu.pack(anchor=CENTER)
    menu.config(bg="black")
    panel.config(bg="black")
    
    menu_carga.after(3000, menu_carga.destroy)

    ventana=Tk()
    ventana.title('Bingo')
    bingo1=Label(ventana)
    ventana.geometry("1920x1080")
    ventana.attributes('-fullscreen', True)
    ventana.config(bg="black")
    
    bingo1.pack()             
    
    text1=Text(ventana,width=47,height=1,bg='grey',padx=900)
    text1.config(font=('Helvetica bold',40))

    text1.pack()
    
    
    can1=Canvas(ventana,width=100,height=70)
    lab1=Label(can1, text=listo[0],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab1.pack()
    lab2=Label(can1, text=listo[1],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab2.pack()
    lab3=Label(can1, text=listo[2],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab3.pack()
    lab4=Label(can1, text=listo[3],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab4.pack()
    lab5=Label(can1, text=listo[4],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab5.pack()
    can1.pack(side=LEFT)

    can2=Canvas(ventana,width=100,height=70)
    lab6=Label(can2, text=listo[5],width=5,borderwidth=4, relief="solid", font=('Bold',80))
    lab6.pack()
    lab7=Label(can2, text=listo[6],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab7.pack()
    lab8=Label(can2, text=listo[7],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab8.pack()
    lab9=Label(can2, text=listo[8],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab9.pack()
    lab10=Label(can2, text=listo[9],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab10.pack()
    can2.pack(side=LEFT)
    
    can3=Canvas(ventana,width=100,height=70)
    lab11=Label(can3, text=listo[10],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab11.pack()
    lab12=Label(can3, text=listo[11],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab12.pack()
    lab13=Label(can3, text=listo[12],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab13.pack()
    lab14=Label(can3, text=listo[13],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab14.pack()
    lab15=Label(can3, text=listo[14],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab15.pack()
    can3.pack(side=LEFT)

    can4=Canvas(ventana,width=100,height=70)
    lab16=Label(can4, text=listo[15],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab16.pack()
    lab17=Label(can4, text=listo[16],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab17.pack()
    lab18=Label(can4, text=listo[17],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab18.pack()
    lab19=Label(can4, text=listo[18],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab19.pack()
    lab20=Label(can4, text=listo[19],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab20.pack()
    can4.pack(side=LEFT)

    can5=Canvas(ventana,width=100,height=70)
    lab21=Label(can5, text=listo[20],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab21.pack()
    lab22=Label(can5, text=listo[21],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab22.pack()
    lab23=Label(can5, text=listo[22],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab23.pack()
    lab24=Label(can5, text=listo[23],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab24.pack()
    lab25=Label(can5, text=listo[24],width=5,borderwidth=4, relief="solid",font=('Bold',80))
    lab25.pack()

    can5.pack(side=LEFT)
    
    bot1=Button(ventana,text='Cerrar',height=5,width=15,fg="red",bg="black",activebackground="black",font=('Helvetica bold',20),command=ventana.quit)
    bot1.place(relx = 0.850, rely = 0.25)
    bot2=Button(ventana,text='Dibujar un número',height=5,width=15,fg="red",bg="black",activebackground="black",font=('Helvetica bold',20),command=numeros_random)
    bot2.place(relx = 0.850, rely = 0.45)
    bot3=Button(ventana,text='Tachar el número',height=5,width=15,fg="red",bg="black",activebackground="black",font=('Helvetica bold',20),command=elim_nums)
    bot3.place(relx = 0.850, rely = 0.65)
    
    ventana.mainloop()
import menu