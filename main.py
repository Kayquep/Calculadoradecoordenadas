import tkinter as tk
from tkinter import font  as tkfont
import math



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True,)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



#GMS to decimal
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def proces():
            lad = tk.Entry.get(E1)
            lam = tk.Entry.get(E5)
            las = tk.Entry.get(E6)
            lod = tk.Entry.get(E2)
            lom = tk.Entry.get(E7)
            los = tk.Entry.get(E8)

            resultado = float(lad) + (((float(lam) / 60)) + ((float(las) / 3600)))
            resultado2 = float(lod) + (((float(lom) / 60)) + ((float(los) / 3600)))
            E3.config(state='normal')
            E4.config(state='normal')

            tk.Entry.delete(E3, 0, 'end')
            tk.Entry.insert(E3, 0, resultado)
            tk.Entry.delete(E4, 0, 'end')
            tk.Entry.insert(E4, 0, resultado2)

        L1 = tk.Label(self, text="Control Calc", )
        L1.grid(row=0, column=1)
        L1.place(relx=0.5, rely=0)
        L2 = tk.Label(self, text="Latitude", )
        L2.grid(row=1, column=1)
        L2.place(relx=0.2, rely=0.1)
        L3 = tk.Label(self, text="Longitude", )
        L3.grid(row=2, column=1)
        L3.place(relx=0.2, rely=0.2)
        L4 = tk.Label(self, text="Latitude", )
        L4.grid(row=3, column=1)
        L4.place(relx=0.2, rely=0.3)
        L8 = tk.Label(self, text="Longitude", )
        L8.grid(row=4, column=1)
        L8.place(relx=0.2, rely=0.4)
        L5 = tk.Label(self, text="°", font="Arial", )
        L5.grid(row=1, column=1)
        L5.place(relx=0.56, rely=0.1)
        L6 = tk.Label(self, text="'", font="Arial", )
        L6.grid(row=1, column=1)
        L6.place(relx=0.67, rely=0.1)
        L7 = tk.Label(self, text="''", font="Arial", )
        L7.grid(row=1, column=1)
        L7.place(relx=0.8, rely=0.1)
        L8 = tk.Label(self, text="°", font="Arial", )
        L8.grid(row=1, column=1)
        L8.place(relx=0.56, rely=0.2)
        L9 = tk.Label(self, text="'", font="Arial", )
        L9.grid(row=1, column=1)
        L9.place(relx=0.67, rely=0.2)
        L10 = tk.Label(self, text="''", font="Arial", )
        L10.grid(row=1, column=1)
        L10.place(relx=0.8, rely=0.2)

        E1 = tk.Entry(self, bd=2, width=3)
        E1.grid(row=1, column=1)
        E1.place(relx=0.5, rely=0.1)
        E2 = tk.Entry(self, bd=2, width=3)
        E2.grid(row=2, column=1)
        E2.place(relx=0.5, rely=0.2)
        E3 = tk.Entry(self, bd=2)
        E3.grid(row=3, column=1)
        E3.place(relx=0.5, rely=0.3)
        E3.config(state='disable')
        E4 = tk.Entry(self, bd=2)
        E4.grid(row=4, column=1)
        E4.place(relx=0.5, rely=0.4)
        E4.config(state='disable')
        E5 = tk.Entry(self, bd=2, width=3, )
        E5.grid(row=1, column=1, )
        E5.place(relx=0.6, rely=0.1)
        E6 = tk.Entry(self, bd=2, width=6)
        E6.grid(row=1, column=1)
        E6.place(relx=0.7, rely=0.1)
        E7 = tk.Entry(self, bd=2, width=3, )
        E7.grid(row=1, column=1, )
        E7.place(relx=0.6, rely=0.2)
        E8 = tk.Entry(self, bd=2, width=6)
        E8.grid(row=1, column=1)
        E8.place(relx=0.7, rely=0.2)
        B = tk.Button(self, text="Converter", command=proces)
        B.grid(row=1, column=1, )
        B.place(relx=0.5, rely=0.5)


        new_order = (E1, E5, E6, E2, E7, E8)
        for widget in new_order:
            widget.lift()


        gms = tk.Radiobutton(self, text='Graus minutos segundos',value=1, command=lambda: controller.show_frame("StartPage"))
        gms.grid(row=1, column=1)
        gms.place(relx=0.5, rely=0.6)
        gms.select()
        gmd = tk.Radiobutton(self, text='Graus minutos decimais',value=2, command=lambda: controller.show_frame("PageOne"))
        gmd.grid(row=1, column=1)
        gmd.place(relx=0.5, rely=0.7)


#GM to decimal
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def proces():
            lad = tk.Entry.get(E1)
            lam = tk.Entry.get(E5)
            lod = tk.Entry.get(E2)
            lom = tk.Entry.get(E7)

            resultado = int(lad) + ((float(lam) / 60))
            resultado2 = int(lod) + ((float(lom) / 60))
            E3.config(state='normal')
            E4.config(state='normal')

            tk.Entry.delete(E3, 0, 'end')
            tk.Entry.insert(E3, 0, resultado)
            tk.Entry.delete(E4, 0, 'end')
            tk.Entry.insert(E4, 0, resultado2)

        L1 = tk.Label(self, text="Calculadora de Coordenadas", )
        L1.grid(row=0, column=1)
        L1.place(relx=0.5, rely=0)
        L2 = tk.Label(self, text="Latitude", )
        L2.grid(row=1, column=1)
        L2.place(relx=0.2, rely=0.1)
        L3 = tk.Label(self, text="Longitude", )
        L3.grid(row=2, column=1)
        L3.place(relx=0.2, rely=0.2)
        L4 = tk.Label(self, text="Latitude", )
        L4.grid(row=3, column=1)
        L4.place(relx=0.2, rely=0.3)
        L8 = tk.Label(self, text="Longitude", )
        L8.grid(row=4, column=1)
        L8.place(relx=0.2, rely=0.4)
        L5 = tk.Label(self, text="°", font="Arial", )
        L5.grid(row=1, column=1)
        L5.place(relx=0.56, rely=0.1)
        L6 = tk.Label(self, text="'", font="Arial", )
        L6.grid(row=1, column=1)
        L6.place(relx=0.73, rely=0.1)
        L8 = tk.Label(self, text="°", font="Arial", )
        L8.grid(row=1, column=1)
        L8.place(relx=0.56, rely=0.2)
        L9 = tk.Label(self, text="'", font="Arial", )
        L9.grid(row=1, column=1)
        L9.place(relx=0.73, rely=0.2)

        E1 = tk.Entry(self, bd=2, width=3)
        E1.grid(row=1, column=1)
        E1.place(relx=0.5, rely=0.1)
        E2 = tk.Entry(self, bd=2, width=3)
        E2.grid(row=2, column=1)
        E2.place(relx=0.5, rely=0.2)
        E3 = tk.Entry(self, bd=2)
        E3.grid(row=3, column=1)
        E3.place(relx=0.5, rely=0.3)
        E3.config(state='disable')
        E4 = tk.Entry(self, bd=2)
        E4.grid(row=4, column=1)
        E4.place(relx=0.5, rely=0.4)
        E4.config(state='disable')
        E5 = tk.Entry(self, bd=2, width=8, )
        E5.grid(row=1, column=1, )
        E5.place(relx=0.6, rely=0.1)
        E7 = tk.Entry(self, bd=2, width=8, )
        E7.grid(row=1, column=1, )
        E7.place(relx=0.6, rely=0.2)
        B = tk.Button(self, text="Converter", command=proces)
        B.grid(row=1, column=1, )
        B.place(relx=0.5, rely=0.5)

        new_order = (E1, E5, E2, E7)
        for widget in new_order:
            widget.lift()
        gms = tk.Radiobutton(self, text='Graus minutos segundos', value=1,
                             command=lambda: controller.show_frame("StartPage"))
        gms.grid(row=1, column=1)
        gms.place(relx=0.5, rely=0.6)
        gms.select()
        gmd = tk.Radiobutton(self, text='Graus minutos decimais', value=2,
                             command=lambda: controller.show_frame("PageOne"))
        gmd.grid(row=1, column=1)
        gmd.place(relx=0.5, rely=0.7)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def proces():
            lade = tk.Entry.get(E3)
            lod = tk.Entry.get(E4)
            lom = tk.Entry.get(E7)
            los = tk.Entry.get(E8)
            lam, lad = math.modf(E3)
            las, x = math.modf(lam)

            lame = float(lam*60)
            lase = float(las*60)
            E3.config(state='normal')
            E4.config(state='normal')

            tk.Entry.delete(E5, 0, 'end')
            tk.Entry.insert(E5, 0, lad)
            tk.Entry.delete(E6, 0, 'end')
            tk.Entry.insert(E6, 0, lame)
            tk.Entry.delete(E7, 0, 'end')
            tk.Entry.insert(E7, 0, lase)

        L1 = tk.Label(self, text="Control Calc", )
        L1.grid(row=0, column=1)
        L1.place(relx=0.5, rely=0)
        L2 = tk.Label(self, text="Latitude", )
        L2.grid(row=1, column=1)
        L2.place(relx=0.2, rely=0.1)
        L3 = tk.Label(self, text="Longitude", )
        L3.grid(row=2, column=1)
        L3.place(relx=0.2, rely=0.2)
        L4 = tk.Label(self, text="Latitude", )
        L4.grid(row=3, column=1)
        L4.place(relx=0.2, rely=0.3)
        L8 = tk.Label(self, text="Longitude", )
        L8.grid(row=4, column=1)
        L8.place(relx=0.2, rely=0.4)
        L5 = tk.Label(self, text="°", font="Arial", )
        L5.grid(row=1, column=1)
        L5.place(relx=0.56, rely=0.3)
        L6 = tk.Label(self, text="'", font="Arial", )
        L6.grid(row=1, column=1)
        L6.place(relx=0.67, rely=0.3)
        L7 = tk.Label(self, text="''", font="Arial", )
        L7.grid(row=1, column=1)
        L7.place(relx=0.8, rely=0.3)
        L8 = tk.Label(self, text="°", font="Arial", )
        L8.grid(row=1, column=1)
        L8.place(relx=0.56, rely=0.4)
        L9 = tk.Label(self, text="'", font="Arial", )
        L9.grid(row=1, column=1)
        L9.place(relx=0.67, rely=0.4)
        L10 = tk.Label(self, text="''", font="Arial", )
        L10.grid(row=1, column=1)
        L10.place(relx=0.8, rely=0.4)

        E1 = tk.Entry(self, bd=2, width=3)
        E1.grid(row=1, column=1)
        E1.place(relx=0.5, rely=0.3)
        E1.config(state='disable')
        E2 = tk.Entry(self, bd=2, width=3)
        E2.grid(row=2, column=1)
        E2.place(relx=0.5, rely=0.4)
        E2.config(state='disable')
        E3 = tk.Entry(self, bd=2)
        E3.grid(row=3, column=1)
        E3.place(relx=0.5, rely=0.1)
        E4 = tk.Entry(self, bd=2)
        E4.grid(row=4, column=1)
        E4.place(relx=0.5, rely=0.2)
        E5 = tk.Entry(self, bd=2, width=3, )
        E5.grid(row=1, column=1, )
        E5.place(relx=0.6, rely=0.3)
        E5.config(state='disable')
        E6 = tk.Entry(self, bd=2, width=6)
        E6.grid(row=1, column=1)
        E6.place(relx=0.7, rely=0.3)
        E6.config(state='disable')
        E7 = tk.Entry(self, bd=2, width=3, )
        E7.grid(row=1, column=1, )
        E7.place(relx=0.6, rely=0.4)
        E7.config(state='disable')
        E8 = tk.Entry(self, bd=2, width=6)
        E8.grid(row=1, column=1)
        E8.place(relx=0.7, rely=0.4)
        E8.config(state='disable')
        B = tk.Button(self, text="Converter", command=proces)
        B.grid(row=1, column=1, )
        B.place(relx=0.5, rely=0.5)

        new_order = (E1, E5, E6, E2, E7, E8)
        for widget in new_order:
            widget.lift()

        gms = tk.Radiobutton(self, text='Graus minutos segundos', value=1,
                             command=lambda: controller.show_frame("StartPage"))
        gms.grid(row=1, column=1)
        gms.place(relx=0.5, rely=0.6)
        gms.select()
        gmd = tk.Radiobutton(self, text='Graus minutos decimais', value=2,
                             command=lambda: controller.show_frame("PageOne"))
        gmd.grid(row=1, column=1)
        gmd.place(relx=0.5, rely=0.7)
        gd = tk.Radiobutton(self, text='Graus decimais', value=3, command=lambda: controller.show_frame("PageTwo"))
        gd.grid(row=1, column=1)
        gd.place(relx=0.5, rely=0.8)


if __name__ == "__main__":
    app = SampleApp()
    app.geometry('400x300')
    app.title('Calc')
    app.mainloop()
