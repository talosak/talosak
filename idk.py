from tkinter import *

def Command1():
    B = Tk()
    B.title("DELFINY!")
    E = Label(B, text="""Inia jest największym gatunkiem spośród słodkowodnych delfinów. Samce tego gatunku osiągają maksymalnie 2,55 m długości (średnio 2,32 m) i maksymalną wagę 207 kg (średnio 154 kg).\n
    Samice są mniejsze, osiągają do 2,1 m długości (średnio 2 m) i masę nieprzekraczającą 154 kg (średnio 100 kg)[7]. Różnice w wielkości pomiędzy płciami są główną cechą dymorfizmu płciowego u waleni.\n
    Delfin inia jest pod tym względem nietypowy, gdyż to samce są większe niż samice, odwrotnie niż u pozostałych waleni[8]. Kolor skóry zmienia się z wiekiem.\n 
    Młode osobniki są ciemnoszare, z czasem zmieniają odcień na srebrny lub różowy. Samce są intensywniej ubarwione od samic. Niektóre osobniki dorosłe mają ciemniejszy grzbiet - ciemnoróżowy lub nawet brunatny. \n
    Ubarwienie i jego intensywność są w dużej mierze zależne od temperatury i czystości wody oraz od położenia geograficznego[9]. Inie sprawiają wrażenie ociężałych i powolnych, jednak zupełnie niesłusznie. \n
    W przeciwieństwie do budowy układu kostnego delfinów słonowodnych żaden z kręgów szyjny inii nie jest połączony z pozostałymi, dzięki czemu zwierzę ma duże pole ruchu głowy. Płetwy piersiowe są duże, regularne i równobocznie trójkątne. Niekiedy występuje 6 paliczków[8]. """)
    E.pack()
    A.destroy()

def Command2():
    C = Tk()
    C.title("D:")
    D = Label(C, text=":(")
    D.pack()
    A.destroy()

A = Tk()
A.title("??????????????")

Label(A, text="Delfiny???").pack()


Button1 = Button(A, text="TAK", command=Command1)
Button1.pack()
Button2 = Button(A, text="NIE", command=Command2)
Button2.pack()

A.mainloop()
