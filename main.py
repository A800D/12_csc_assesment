from tkinter import *
from PIL import ImageTk, Image


class QuizStarter:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="orange"# to set it as background color for all the label widgets


        self.bg_image= Image.open("supra.png")
        self.bg_image = self.bg_image.resize((450, 250), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color)
        #padx, pady How many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders.
        self.quiz_frame.grid()#This geometry manager organizes widgets in a table-like structure in the parent widget.
       #label image
        self.image_label= Label(self.quiz_frame, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
         
               
        #widgets goes below
        self.heading_label=Label(self.quiz_frame, text="Lets test your car knowledge", font=("Tw Cen MT","18","bold"),bg=background_color)
        self.heading_label.grid(row=0, padx=20) 

        #label for username
        self.user_label=Label(self.quiz_frame, text="Please enter your username below: ", font=("Tw Cen MT","16"),bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20) 
        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)
        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="orange", command=self.name_collection)
        self.continue_button.grid(row=3,  padx=20, pady=20)        

       

    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning
        self.quiz_frame.destroy()







if __name__ == "__main__":
    root = Tk()
    root.title("Lets test your car knowledge") 
    quiz_instance = QuizStarter(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear
 
    

