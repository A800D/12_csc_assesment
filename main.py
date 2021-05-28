from tkinter import *
from PIL import ImageTk, Image


class QuizStarter:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 

        self.bg_image= Image.open("supra.png")
        self.bg_image = self.bg_image.resize((700, 600), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)


       #label image
        self.image_label= Label(parent, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
         
               
        
        #entry box
        self.entry_box=Entry(parent)
        self.entry_box.place(x=70, y=350)
      




        #continue button
        self.continue_button = Button(parent, text="Continue", font=("Helvetica", "30", "bold"), bg="orange", command=self.name_collection)
        self.continue_button.place(x=390, y=430) 

       

    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning
        self.entry_box.destroy()
        self.image_label.destroy()






if __name__ == "__main__":
    root = Tk()
    root.title("Lets test your car knowledge") 
    root.geometry("700x600")
    quiz_instance = QuizStarter(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear
 
    

