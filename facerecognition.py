from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2
from cv2 import *
class Face_Recognition:
   def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\gopal\Desktop\minor project\checkimage.jpg")
        img=img.resize((1366,130))
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\gopal\Desktop\project image\attendence pageimage1.jpg")
        bg1=bg1.resize((1366,768))
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"C:\Users\gopal\Desktop\project image\attendencebutton.jpg")
        std_img_btn=std_img_btn.resize((180,180))
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.std_img1,command=self.face_recog,cursor="hand2")
        std_b1.place(x=600,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,text="Face Detector",command=self.face_recog,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=600,y=350,width=180,height=45)

   def face_recog(self):
       def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                studentid, predict = clf.predict(gray_image[y:y+h, x:x+w])

                confidence = int((100 * (1 - predict/300)))
                conn = mysql.connector.connect(host="localhost", username="root", password="W2002@gopal#", database="face_recognition1")
                cursor = conn.cursor()
                cursor.execute("select name from student3 where studentid=" + str(studentid))
                n = cursor.fetchone()
                print(n)
                n = "+".join(n) if n else "marachoda"  # Handling case when n is None
                cursor.execute("select roll from student3 where studentid=" + str(studentid))
                r = cursor.fetchone()
                r = "+".join(r) if r else "Unknown"  # Handling case when r is None
                cursor.execute("select name from student3 where studentid=" + str(studentid))
                i = cursor.fetchone()
                i = "+".join(i) if i else "Unknown"  # Handling case when i is None

                if confidence > 77:
                   
                    cv2.putText(img, f"Student_ID:{i}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Name:{n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Roll-No:{r}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    print("balchoda")
            # self.mark_attendance(i, r, n)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                coord = [x, y, w, y]
            return coord

       def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
       faceCascade=cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
       clf=cv2.face.LBPHFaceRecognizer_create()
       clf.read("classifier.xml")

       videoCap=cv2.VideoCapture(0)
       while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 13:
                break
       videoCap.release()
       cv2.destroyAllWindows()            


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop() 