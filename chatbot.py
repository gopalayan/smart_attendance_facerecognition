from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

          #******chatbot image***************
        img_chat=Image.open('chatbot.jpg')
        img_chat=img_chat.resize((200,70))
        self.photoimg=ImageTk.PhotoImage(img_chat)

        title_lbl=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='green',bg='white')
        title_lbl.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=5,relief=RAISED,font=('arial',14,),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        button_frame=Frame(self.root,bd=4,bg='white',width=730)
        button_frame.pack()

        label1=Label(button_frame,cursor="hand2",text="Type something",font=('arial',14,'bold'),fg='green',bg='white')
        label1.grid(row=0,column=0,padx=5,sticky=W)
        

        self.entry=StringVar()
        self.entry1=ttk.Entry(button_frame,textvariable=self.entry,cursor="hand2",width=40,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(button_frame,cursor="hand2",command=self.send,text="send>>",font=('arial',15,'bold'),width=7,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(button_frame,cursor="hand2",command=self.clear,text="Clear Data",font=('arial',13,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)
        
        self.msg=''
        self.label_2=Label(button_frame,cursor="hand2",text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label_2.grid(row=1,column=1,padx=5,sticky=W)

        #**************functio declaration*******************
    def enter_func(self,event):
       self.send.invoke()
       self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')


    def send(self):
        send='\t\t\t'+'You:'+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg='please enter some input'
            self.label_2.config(text=self.msg,fg='red')
        else:
            self.msg=''    
            self.label_2.config(text=self.msg,fg='red')

        if (self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')

        elif (self.entry.get()=='how are you?'):
            self.text.insert(END,'\n\n'+'Bot: fine and you')

        elif (self.entry.get()=='who create you?'):
            self.text.insert(END,'\n\n'+'Bot: Mr. Sarkar ')
        elif (self.entry.get()=='what is your name'):
            self.text.insert(END,'\n\n'+'Bot: my name is hacker')
        elif (self.entry.get()=='bye'):
            self.text.insert(END,'\n\n'+'Bot: thank you for chatting')
        
        else:
             self.text.insert(END,'\n\n'+'Bot: sorry I did not get it')






if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()
