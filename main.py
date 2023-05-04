import psutil
import os
import pprint
import platform
from tkinter import *
from tkinter import ttk
        
battery = psutil.sensors_battery()
bat=battery.percent
bat1=battery.power_plugged

def procinfo():
     psutil.virtual_memory()
     psutil.getloadavg()
     psutil.cpu_percent()
     psutil.cpu_percent(percpu=True)
     process_list = []
     for process in psutil.process_iter():
          process_info = process.as_dict(attrs=['name', 'cpu_percent'])
          process_list.append(process_info)
          pprint.pprint(process_list) 

# Getting loadover15 minutes
#load1, load5, load15 = psutil.getloadavg()
#cpu_usage = (load15/os.cpu_count())*100
cpu_usage=psutil.cpu_percent(4)
rampercent=psutil.virtual_memory()[2]
# Getting usage of virtual_memory in GB ( 4th field)
ramgb = psutil.virtual_memory()[3]/1000000000

system = platform.system()
machine = platform.machine()
processor = platform.processor()

class App:
    def __init__(self, master):   
          
          m.title('Power consumption and system monitoring')
          m.geometry("950x800")
          m.configure(bg="White")
          
          head = Label(m,text="-----POWER CONSUMPTION-----",font='verdana',bg="white",fg="Black")#ROW0COL0
          l1 = Label(m,text="BATTERY PERCENT   : ",bg="white",fg="Black")#ROW1COL0
          prg1 = ttk.Progressbar(m,orient = HORIZONTAL,value=f"{bat}",length = 150, mode = 'determinate')
          h1 = Label(m,text=f"{bat}%")
          
          l2 = Label(m,text="PLUGGED YES/NO   : ",bg="white",fg="Black")#ROW2COL0
          t = Label(m,text=f"{bat1}",bg="white",fg="Black")#row2col1

          l3 = Label(m,text="-----SYSTEM MONITORING-----",font='verdana',bg="white",fg="Black")#row3col0
          l4 = Label(m,text="CPU USAGE   : ",bg="white",fg="Black")#row4col0
          prg2 = ttk.Progressbar(m,orient = HORIZONTAL,value=f"{cpu_usage}",length = 150, mode = 'determinate',maximum=100)
          l5 = Label(m,text=f"{cpu_usage:.2f}%")#row4col2

          l8 = Label(m,text="RAM USAGE   : ",bg="white",fg="Black")#row5col0
          prg3 = ttk.Progressbar(m,orient = HORIZONTAL,value=f"{rampercent}",length = 150, mode = 'determinate',maximum=100)
          h2 = Label(m,text=f"{rampercent:.2f}%")

          l7 = Label(m,text="RAM in GB   :",bg="white",fg="Black")#row6col0
          l6 = Label(m,text=f"{ramgb:.2f} GB",bg="white",fg="Black")#row6col1

          button1 = Button(m,text="Process info",relief=SOLID,command=procinfo,foreground="Black",background="White")

          head2 = Label(m,text="-----SYSTEM SPECIFICATIONS----- ",font='verdana',bg="white",fg="Black")
          sys = Label(m,text="System    : ",bg="white",fg="Black")
          mac = Label(m,text="Machine   : ",bg="white",fg="Black")
          pro = Label(m,text="Processor : ",bg="white",fg="Black")
          sys1= Label(m,text=f"{system}",fg="black",bg="white")
          mac1= Label(m,text=f"{machine}",fg="black",bg="white")
          pro1= Label(m,text=f"{processor}",fg="black",bg="white")


          head.grid(row = 0,column = 0,pady=25,padx=75)
          l1.grid(row =1 ,column = 0,pady=2)
          prg1.grid(row=1,column = 1)
          l2.grid(row=2,column=0,pady=2)
          t.grid(row=2,column = 1)
          
          l3.grid(row=3,column=0,pady=25)
          l4.grid(row=4,column=0,pady=2)
          prg2.grid(row=4,column=1,pady=2)
          l5.grid(row=4,column=1,pady=2)
          
          l8.grid(row=5,column=0,pady=2)
          prg3.grid(row=5,column=1,pady=2)
          l7.grid(row=6,column=0,pady=2)
          l6.grid(row=6,column=1,pady=2)
          h1.grid(row=1,column=1)
          h2.grid(row=5,column=1)

          head2.grid(row=7,column=0,pady=25)
          sys.grid(row=8,column=0,pady=2)
          mac.grid(row=9,column=0,pady=2)
          pro.grid(row=10,column=0,pady=2,padx=70)
          
          sys1.grid(row=8,column=1,pady=2)
          mac1.grid(row=9,column=1,pady=2)
          pro1.grid(row=10,column=1,pady=2)
          
          button1.grid(row=11,column=0,pady=25)
          
m= Tk()
m.option_add('*font', ('Bahnschrift', 12))
display = App(m)
m.mainloop()
