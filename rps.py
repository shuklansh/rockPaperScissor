from tkinter import *
import random

window=Tk()
window.title('result ')
window=Canvas(window,width=600,heigh=450)
window.pack()
imagetie=PhotoImage(file='D:\\00000\\poyto\\stuff\\tie.PNG')
imagelose=PhotoImage(file='D:\\00000\\poyto\\stuff\\lose.PNG')
imagewin=PhotoImage(file='D:\\00000\\poyto\\stuff\\win.PNG')



while True:
    s1=str(input(" rock paper or scissor: "))
    rps = ["rock","paper","scissor"]
    s=random.choice(rps)
    s2=str(s)
    if(s1==s2):
        print("tie..")
        window.create_image(0,0, anchor=NW, image=imagetie)
        
        
    else:
        if(s1=="rock"):
            
            
            if(s2=="paper"):
                print("computer: ",s2,"\n you lose :(")
                window.create_image(0,0, anchor=NW, image=imagelose)
                
            elif(s2=="scissor"):
                print("computer : ",s2,"\n you win! :D")
                window.create_image(0,0, anchor=NW, image=imagewin)
            
            
            
        elif(s1=="paper"):
            
            if(s2=="scissor"):
                print("computer: ",s2,"\n you lose :(")
                window.create_image(0,0, anchor=NW, image=imagelose)
               
               
            elif(s2=="rock"):
                print("computer : ",s2,"\n you win! :D")
                window.create_image(0,0, anchor=NW, image=imagewin)
            
            
        elif(s1=="scissor"):
            
            if(s2=="rock"):
                print("computer : ",s2,"\n you lost :(")
                window.create_image(0,0, anchor=NW, image=imagelose)

               
            elif(s2=="paper"):
                print("computer: ",s2,"\n you win! :D")
                window.create_image(0,0, anchor=NW, image=imagewin)

