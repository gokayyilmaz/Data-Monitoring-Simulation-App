# data-monitoring-app-simulation
Dynamic Data Monitoring Simulation Application

# INTRODUCTION
The aim of this project is to develop a dynamic data monitoring application. 
User can measure voltage in 8 channels and get the result. The application has 3 main parts for observe the results. These are dynamic table, dynamic graph and the log file.

# METHOD
The program works in 3 main stages :
(Please read the important notes section which is at the bottom of this report, before working with program.)

1)	User can select channels and press START button for measuring.

2)	During the measurement user can observe results from table and graph.

3)	User can stop the mesaurement with pressing STOP button, After that, the log file can be examined.

Additionally, user can see the user manual with pressing OPEN USER MANUAL button whenever he/she wants.

# CONCLUSION
That was an instructive project for me when applying my Python theoretical knowladge to the real world application. It is also entertaining, because creating a GUI application is more lively than making a console-based one. 
In real world and in my Electrical Engineering Design project, I use PySerial extension and show real data coming from serial port rather than random numbers between 0 and 10. This course and this project help me learning PyQt and finishing my EE Design project in a more robust and quicker way.

# IMPORTANT NOTES
1)	For using the application and the matplotlib library with full functionality:
Please, use the program with WinPython distribution and Spyder IDE. In WinPython / Spyder IDE, Go to Tools >> Preferences >> IPython console >> Graphics >> Backend:Inline, change "Inline" to "Qt5", click "OK".

2)	This application is a simulation. Because of that it uses random numbers between 0 and 10 rather than real sensor measurements. The program updates table and graph with average of 1000 fictional measurement samples for observing live results with human eye better.  Because of taking average of the pseudorandom numbers, table and graph values just about to 5 everytime. 
