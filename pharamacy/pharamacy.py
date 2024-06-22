from tkinter import*
from PIL import Image.ImageTK


class PharamacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title('pharamacy Management System')
        self.root.geometry('1300x500+0+0')

        lbltitle=Label(self.root,text='PHARAMACY MANAGEMENT SYSTEM',bd=15,
                   relief=RIDGE,bg='white',fg='darkgreen',font=('times new roman',40,'bold'),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)



        img1=Image.open("pharamacy_logo.jpg")
        img1=img1.resize((80,80),Image.ANTIALIAS)
        self.photoimg1=ImageTK.photoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=20)






if __name__=='__main__':
    root=Tk()
    obj=PharamacyManagementSystem(root)
    root.mainloop()