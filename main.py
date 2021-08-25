from tkinter import *
import webbrowser ,time ,pyautogui
from tkinter import ttk
root=Tk()
root.geometry("600x100")
root.configure(bg='cyan')
l=Label(root,text="Enter meet code", font = ('Consolas', 10, 'bold'), bg = 'cyan')
l.grid(row=0,column=0)
l2 = Label(root, text = "Enter time ", font=('Consolas', 10,'bold'),bg = 'cyan')
l2.grid(row=0,column=1)

v = StringVar(root, value='aaa-bbbb-ccc')
url_entry=Entry(root, font = ('arial'), textvariable=v)

#url_entry.set("aaa-bbbb-ccc")

url_entry.grid(row=1,column=0,padx=15,pady=5)
hrs =["0","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
clicked1 = StringVar()
clicked1.set( "hrs" )
#hour is combobox name 
hour= ttk.Combobox( root , textvariable=clicked1 , values=hrs )
hour.grid(row=1,column=1)
mns =["0","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60",]
clicked2 = StringVar()
clicked2.set( "mns" )
#min is combobox name 
min = ttk.Combobox( root , textvariable=clicked2 , values=mns )
min.grid(row=1,column=2)
photo = PhotoImage(file = "meetjoiner.png")
root.title("MEET JOINER")
root.iconphoto(False, photo)

def button():
    url=url_entry.get()
    hours=hour.get()
    mins=min.get()
    alarm_time=hours+":"+mins
    Current_time = time.strftime("%H:%M")
    while Current_time !=alarm_time:
        Current_time = time.strftime("%H:%M")
        print("😭")
        time.sleep(5)
    if Current_time ==alarm_time:
        webbrowser.open('https://meet.google.com/' + url)
        time.sleep(10)
        pyautogui.click(x=490, y=309)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'd')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'e')
        time.sleep(2)
        pyautogui.hotkey('tab')#1
        pyautogui.hotkey('tab')#2
        pyautogui.hotkey('tab')#3
        pyautogui.hotkey('tab')#4
        pyautogui.hotkey('tab')#5
        pyautogui.hotkey('tab')#6
        #pyautogui.hotkey('tab')#7
        #pyautogui.hotkey('tab')#8
        time.sleep(4)
        pyautogui.hotkey('enter')
    
photo2 = PhotoImage(file="start.png")
bt=Button(root,image=photo2,command=button, border = 0)
bt.grid(row=2,column=1,padx=5,pady=5)




root.mainloop()