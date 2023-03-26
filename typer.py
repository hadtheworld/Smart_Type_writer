import keyboard
import tkinter as tk
from chat_gpt_bot import chat
class check_box:
    rec=[]
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.root=tk.Tk()
        self.canvas1=tk.Canvas(self.root,width=self.x,height=self.y)
        self.canvas1.pack()  
        self.entry=tk.Entry(self.root)
        self.canvas1.create_window(self.x//2,self.y-(self.y//10),window=self.entry)
        self.text=tk.Text(height=25, width=50)
        self.canvas1.create_window(self.x//2,self.y-(self.y/(1.7)),window=self.text)
        self.root.title("Enter inour number ans press Enter to cintunue!!:\nctrl+y to start\nctrl+k to stop and restart")
        self.button1=tk.Button(text='YES',command=self.execute)
        self.canvas1.create_window((self.x//2)-((self.x//2)//2),self.y-(self.y//10),window=self.button1)
        self.button2=tk.Button(text='NO',command=self.root.destroy)
        self.canvas1.create_window((self.x//2)+((self.x//2)//2),self.y-(self.y//10),window=self.button2)
    def CheckBox(self):
        self.root.mainloop()
    def make_chat(self,inp):
        text_inp=self.text.get("1.0","end-1c")
        output=chat(text_inp)
        obj=TypeWriter(inp)
        obj.file_write(output)
    def execute(self):
        inp=int(self.entry.get())
        self.make_chat(inp)
        if inp<1 or inp>10:
            print("wrong input")
            return
        while (True):
            if (keyboard.is_pressed("ctrl+y")):
                obj=TypeWriter(inp)
                obj.write()
                break
            if(keyboard.is_pressed("ctrl+k")):
                return
    

class TypeWriter:
    def __init__(self,b):
        self.file_number=b
    def file_write(self,content):
        fl_name="input"+str(self.file_number)+".txt"
        file_wr=open(fl_name,'w')
        file_wr.write(content)
        file_wr.close()
    def write(self):
        c="input"+str(self.file_number)+".txt"
        file=open(c,'r')
        s=""
        for i in file:
            s+=i 
        keyboard.write(s)
        file.close()
window=check_box(700,700)
window.CheckBox()