# Sample-Absorbance-GUI

## Project Title
ODE Solver GUI for Bouguer-Beer-Lambert Law 

## Project Overview 
The goal of this project is to construct a Graphical User Interface (GUI) which includes an Ordinary Differential Equation (ODE) solver to solve for the Bouguer-Beer-Lambert Law equation which calculates the decay of irradiation intensity vs path length when light passes through a solution sample in a cuvette. The differential equation was derived through integration and rearrangement of the original equation and solved using the integrate.odeint method in Python. FigureCanvasTkAgg was the canvas object used to integrate the matplotlib graph that was plotted into the Tkinter GUI window. 

## Business Understanding
This project was part of an educational learning experience and evaluation in an introductory course to GUI and ODE modeling and applications. However, the application of this GUI, if developed for commercial use would likely be complimentary to existing spectrometry hardware such as UV-Vis Spectrometers used in chemistry research/teaching laboratories. The GUI allows users to simulate and solve for the equation commonly used to calculate radiative decay and absorbance of a sample if when given specific values of the other parameters such as incident radiation and path length 

## Modeling and Evaluation 
An example of the GUI is shown below. The GUI allows the user to enter various parameters of their sample and test conditions such as molar absorption coefficient, concentration, path length and incident radiation flux. 

![image](https://github.com/kayneong/Sample-Absorbance-GUI/assets/150570357/909d1bb4-8712-4687-9819-79bc275c40e2)

This generates a plot that shows the decay of irradiation intensity against the path length (Length of the cuvette holding the sample solution) as seen below. 

![image](https://github.com/kayneong/Sample-Absorbance-GUI/assets/150570357/085c8f69-7c0f-4c54-991c-7f4664996ba6)


## Conclusion 
This project explored the application of ODE solvers used in traditional chemistry equations as well as its integration into a neat and compact GUI for user application. The graph viewed on the Tkinter GUI also allows for more functions than a usual graph plotted on python consoles such as saving the figure, panning, zooming and configuration. 
