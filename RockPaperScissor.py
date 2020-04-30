import tkinter
import tkinter.messagebox as box
import random

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("200x200")

        # Create two frames. One for the Radiobuttons
        # and another for the regular Button widgets.
        self.radioFrame = tkinter.Frame(self.mainWindow)
        # self.middle_frame = tkinter.Frame(self.main_window)
        self.buttonFrame = tkinter.Frame(self.mainWindow)

        # Create an IntVar object to use with
        # the Radiobuttons.
        self.radioVar = tkinter.StringVar()

        # Set the intVar object to 1.
        self.radioVar.set(1)

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(self.radioFrame, text='rock', variable=self.radioVar, value='rock')
        self.rb2 = tkinter.Radiobutton(self.radioFrame, text='paper', variable=self.radioVar, value='paper')
        self.rb3 = tkinter.Radiobutton(self.radioFrame, text='scissors', variable=self.radioVar, value='scissors')

        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Set up buttons
        self.okButton = tkinter.Button(self.buttonFrame, text='OK', command=self.showOption)
        self.quitButton = tkinter.Button(self.buttonFrame, text='Quit', command=self.mainWindow.destroy)

        # Pack the Buttons.
        self.okButton.pack(side='left')
        self.quitButton.pack(side='left')

        # Pack the frames.
        self.radioFrame.pack()
        self.buttonFrame.pack()

        # Start the mainloop.
        tkinter.mainloop()


    def showOption(self):
        computerChoice = random.randrange(3)
        print(computerChoice)
        if computerChoice == 0:
            choice = 'paper'
            #box.showinfo('Computer choice is :' , choice)
        elif computerChoice ==1:
            choice = 'scissor'
            #box.showinfo('Computer choice is :', choice)
        elif computerChoice ==2:
            choice = 'rock'
            #box.showinfo('Computer choice is :', choice)


        #box.showinfo('Selection',('Computer selected: ' + choice ,'\n','You selected:' + self.radioVar.get()))


#winner statements 
        if choice == 'paper' and self.radioVar.get() == 'scissors':
            print('True')
            box.showinfo('Player wins',('Computer selected: ' + choice ,'\n','You selected:' + self.radioVar.get()))
            print('True')
        elif choice == 'paper' and self.radioVar.get() == 'rock':
            print('True')
            box.showinfo('Computer wins',('Computer selected: ' + choice ,'\n','You selected:' + self.radioVar.get()))
        elif choice == 'paper' and self.radioVar.get() == 'paper':
            print('True')
            box.showinfo('Tie',('Computer selected: ' + choice ,'\n','You selected:' + self.radioVar.get()))
        if choice == 'scissors' and self.radioVar.get() == 'scissors':
            box.showinfo('Tie',('Computer selected: ' + choice ,'\n','You selected:' + self.radioVar.get()))
        elif choice == 'scissors' and self.radioVar.get() == 'rock':
            box.showinfo('Player wins',('Computer selected: ' + choice ,'\n','You selected:' + self.radioVar.get()))
        elif choice == 'scissors' and self.radioVar.get() == 'paper':
            box.showinfo('Computer wins',('Computer selected: ' + choice ,'\n','You selected:' + self.radioVar.get()))
        if choice == 'rock' and self.radioVar.get() == 'rock':
            box.showinfo('Tie',('Computer selected: ' + choice ,'\n','You selected:' + self.radioVar.get()))
        elif choice == 'rock' and self.radioVar.get() == 'paper':
            box.showinfo('Player wins',('Computer selected: ' + choice ,'\n','You selected:' + self.radioVar.get()))
        elif choice == 'rock' and self.radioVar.get() == 'scissors':
            box.showinfo('Computer wins',('Computer selected: ' + choice ,'\n','You selected:' + self.radioVar.get()))


demoGUI = MyGUI()
