import socket
from tkinter import *
from threading import Thread
import random
from PIL import ImageTk,Image

screen_width=None
screen_height=None

server=None
port=None
ip_address=None

playerName=None

canvas1=None
canvas2=None
NameEntry=None
nameWindow=None
gameWindow=None

leftBoxes=[]
rightBoxes=[]
finishBoxes=None

playerType=None
playerTurn=None

player1Name='joining....'
player2Name='joining......'
player1Label=None
player2Label=None
player1Score=0
player2Score=0

player1Scorelabel=None
player2Scorelabel=None

dice=None
rollButton=None
resetButton=None
winningMessage=None

def welcomeScreen():
    global NameEntry,nameWindow,canvas1,playerName

    nameWindow=Tk()
    nameWindow.title("welcome!")
    nameWindow.attributes('-fullscreen',True)

    screen_width=nameWindow.winfo_screenwidth()
    screen_height=nameWindow.winfo_screenheight()

    canvas1=Canvas(nameWindow,width=500,height=500)
    canvas1.pack(fill="both",expand=True)

    bg=ImageTk.PhotoImage(file='background.png')
    canvas1.create_image(0,0,image=bg,anchor="nw")
    canvas1.create_text(screen_width/2,screen_height/5,text="ENTER YOUR NAME",font=("Chalkboard SE",80),fill="white")
    
    NameEntry=Entry(nameWindow,width=15,justify="center",font=("Chalkboard SE",50),bd=5,bg='white')
    NameEntry.place(x=screen_width/2-230,y=screen_height/2-200)

    button=Button(nameWindow,text="Save",font=("Chalkboard SE",20),width=12,height=1,bg="green",bd=1,command=navigate_gameRoom)
    button.place(x=screen_width/2-200,y=screen_height/2-50)
    
    print(screen_width,screen_height)
    nameWindow.mainloop()


def create_leftboxes():
    global gameWindow,leftBoxes,screen_height,screen_width

    xpos=10
    for box in range(0,11):
        if(box == 0):
            boxLabel=Label(gameWindow,font=("Chalkboard SE",30),width=1,height=1,relief='ridge',bg="red",borderwidth=0)
            boxLabel.place(x=xpos,y=screen_height/2 - 100)
            leftBoxes.append(boxLabel)
            xpos+=30
        else:
            boxLabel=Label(gameWindow,font=("Chalkboard SE",30),width=1,height=1,relief='ridge',bg="white",borderwidth=0)
            boxLabel.place(x=xpos,y=screen_height/2 - 100)
            leftBoxes.append(boxLabel)
            xpos+=55

def create_rightboxes():
    global gameWindow,rightBoxes,screen_height,screen_width

    xpos=1300
    for box in range(0,11):
        if(box == 10):
            boxLabel=Label(gameWindow,font=("Chalkboard SE",30),width=1,height=1,relief='ridge',bg="green",borderwidth=0)
            boxLabel.place(x=xpos,y=screen_height/2 - 100)
            rightBoxes.append(boxLabel)
            xpos+=30
        else:
            boxLabel=Label(gameWindow,font=("Chalkboard SE",30),width=1,height=1,relief='ridge',bg="white",borderwidth=0)
            boxLabel.place(x=xpos,y=screen_height/2 - 100)
            rightBoxes.append(boxLabel)
            xpos+=55

def homebox():
    global gameWindow,finishBoxes,screen_height,screen_width

    finishBoxes=Label(gameWindow,text="home",font=("Chalkboard SE",30),width=5,height=0,borderwidth=2,bg="green",fg="white")
    finishBoxes.place(x=screen_width/2-50 , y=screen_height/2-80)

def gameScreen():
    global playerName,screen_height,screen_width,canvas2,player1Label,player2Label,player1Score,player2Score,player1Scorelabel,player2Scorelabel
    global gameWindow,player1Name,player2Name,rollButton,resetButton,winningMessage,resetButton,dice

    gameWindow=Tk()
    gameWindow.title("Game")
    gameWindow.attributes('-fullscreen',True)

    screen_width=gameWindow.winfo_screenwidth()
    screen_height=gameWindow.winfo_screenheight()

    canvas2=Canvas(gameWindow,width=500,height=500)
    canvas2.pack(fill="both",expand=True)
    
    bg=ImageTk.PhotoImage(file='background.png')
    canvas2.create_image(0,0,image=bg,anchor="nw")
    canvas2.create_text(screen_width/2,screen_height/5+100,text="ENTER YOUR NAME",font=("Chalkboard SE",70),fill="white")

    rollButton=Button(gameWindow,text="roll a dice",font=("Chalkboard SE",20),width=12,height=1,bg="white",bd=1)
    rollButton.place(x=screen_width/2-100,y=screen_height/2+150)

    dice=canvas2.create_text(screen_width/2,screen_height/2+50,text='\u2681',font=("Chalkboard SE",100),fill="white")

    player1Label=canvas2.create_text(screen_width/6,screen_height/2-400,text='bibob',font=("Chalkboard SE",100),fill="white")
    player2Label=canvas2.create_text(screen_width/6+1300,screen_height/2-400,text='bobib',font=("Chalkboard SE",100),fill="white")

    player1Scorelabel=canvas2.create_text(screen_width/6,screen_height/2-300,text=player1Score,font=("Chalkboard SE",100),fill="white")
    player2Scorelabel=canvas2.create_text(screen_width/6+1300,screen_height/2-300,text=player2Score,font=("Chalkboard SE",100),fill="white")

    resetButton=Button(gameWindow,text="reset luh game",font=("Chalkboard SE",20),width=12,height=1,bg="white",bd=1)
    resetButton.place(x=screen_width/2-100,y=screen_height/2+250)


    create_leftboxes()
    create_rightboxes()
    homebox()
    gameWindow.mainloop()
#gameScreen()

def navigate_gameRoom():
    global SERVER,nameWindow,NameEntry,playerName
    playerName=NameEntry.get()
    NameEntry.delete(0,END)
    nameWindow.destroy()
    SERVER.send(playerName.encode())
    gameScreen()

def setup():
    global SERVER,PORT,ip_address
    ip_address='127.0.0.1'
    port=8000
    SERVER= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((ip_address,port))
    welcomeScreen()

setup()