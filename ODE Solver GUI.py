# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 17:04:07 2022

@author: kayne
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import log

class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Molar absorption coefficent')
        self.lbl2 = Label(win, text='Concentration (M)')
        self.lbl3 = Label(win, text='Path length (cm)')
        self.lbl4 = Label(win, text='Incident Radiant flux (W)')
        self.e1 = Entry()
        self.e2 = Entry()
        self.e3 = Entry()
        self.e4 = Entry()
        self.b1 = Button(win, text ='Solve', command=self.input)
        self.lbl1.place(x=20, y=50)
        self.e1.place(x=200, y=50)
        self.lbl2.place(x=20, y=100)
        self.e2.place(x=200, y=100)
        self.lbl3.place(x=20, y=150)
        self.e3.place(x=200, y=150)
        self.lbl4.place(x=20, y=200)
        self.e4.place(x=200, y=200)
        self.b1.place(x=170, y=250)
        
    def input(self):
        if len(self.e1.get()) == 0:
            messagebox.showerror("Error", "Please fill up all entries")
        elif len(self.e2.get()) == 0:
            messagebox.showerror("Error", "Please fill up all entries")
        elif len(self.e3.get()) == 0:
            messagebox.showerror("Error", "Please fill up all entries")
        elif len(self.e4.get()) == 0:
            messagebox.showerror("Error", "Please fill up all entries")
        elif float(self.e2.get()) >= 0.00001:
            response = messagebox.askquestion('Question', 'Concentration is too high (>0.00001), accuracy may be affected. Do you wish to continue?')
            if response == 'yes':
              epsilon = float(self.e1.get())
              concentration = float(self.e2.get())
              path_length = float(self.e3.get())
              incident_light = float(self.e4.get())
              k = epsilon*log(10)
              c = concentration
          #initial value
              y0 = incident_light
          
              x = np.linspace(0, path_length,100)
          
          #function that returns dy/dx
              def model(y,x,k,c):
                  dydx = -k*c*y
                  return dydx

              y = integrate.odeint(model, y0, x, args=(k,c))
          
              ode_plot = plt.plot(x, y)
              plt.xlabel('Path length (cm)')
              plt.ylabel('I(x) (W)')
              plt.title('Decay of Radiation flux')
              plt.grid()
              graph_1 = FigureCanvasTkAgg(ode_plot, self)
              graph_1.show()
            else:
              pass
        else:
            epsilon = float(self.e1.get())
            concentration = float(self.e2.get())
            path_length = float(self.e3.get())
            incident_light = float(self.e4.get())
            k = epsilon*log(10)
            c = concentration
        #initial value
            y0 = incident_light
        
            x = np.linspace(0, path_length,1000)
        
        #function that returns dy/dx
            def model(y,x,k,c):
                dydx = -k*c*y
                return dydx

        y = integrate.odeint(model, y0, x, args=(k,c))
        
        ode_plot = plt.plot(x, y)
        plt.xlabel('Path length (cm)')
        plt.ylabel('I(x) (W)')
        plt.title('Decay of Radiation flux')
        plt.grid()
        graph_1 = FigureCanvasTkAgg(ode_plot, self)
        graph_1.show()
        
window=Tk()
mywin=MyWindow(window)
window.wm_title('Bouguer-Lambert-Beer Law Solver')
window.geometry('400x300')
window.mainloop()