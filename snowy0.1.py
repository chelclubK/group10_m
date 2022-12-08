from time import *
from tkinter import *
from random import *
from tkinter import messagebox as mb

s = 128

hp = 3
points = 0
win = 20
dx=[0,1,0,-1]
dy=[1,0,-1,0]
lt=0


def shoot():
    global hX, hY, bonus, fX, fY, enX, enY
    a,b=ground.coords(buLx1)
    
    ground.coords(buLx1,enX*128, enY*128)

    for i in range(1,4):
        sleep(5)
        ground.move(buLx1,i*128,0)
        ground.move(buLx2,i*-128,0)
        ground.move(buLy1,0,i*128)
        ground.move(buLy2,0,i*-128)
            

def check():
    flag=False
    global hX, hY, bonus, fX, fY, enX, enY
    for k in range(4):
        a,b=ground.coords(buL[k])
        if a==hX*s and b==hY*s:
            flag=True
    return flag
            
        
    
def vy():
    global hX, hY, bonus, fX, fY, enX, enY, lt, hp,lives
    
    
        
    lt += 1
    for k in range(4):
        ground.move(buL[k],128*dx[k],128*dy[k])

    if check():
        hp-=1
        lives[hp].destroy()
        if hp == 0:
            ot=mb.askyesno('you dead','try again')
            if ot:
                hp = 3
                points = 0
                point1.config(text=points)
                lives=[]
                for q in range (hp):
                        
                        label1 = Label(main, image = heart, bg="grey")
                        label1.pack(side = LEFT)
                        lives.append(label1)
                
            else:
                main.destroy()
                exit()   

    
    if lt > 9:
        lt = 0
        enX = randint(0,9)
        enY = randint(0,5)
        ground.coords(en,enX*128,enY*128)
        
        for k in range(4):
            ground.coords(buL[k],enX*128, enY*128)
    main.after(500,vy)


def spawn():
    global hX, hY, bonus, fX, fY, enX, enY, hod
    
    
    enX = randint(0,9)
    enY = randint(0,5)
    ground.coords(en,enX*128,enY*128)

    main.after(5000,spawn)


def move(event):
    global hX, hY, bonus, fX, fY, enX, enY, hod, points
    if event.keysym == 'Right' and hX != 9:
            ground.move(hero,s,0)
            hX += 1

    if event.keysym == 'Left'and hX != 0 :
            ground.move(hero,-s,0)
            hX -= 1

    if event.keysym == 'Up'and hY !=  0:
            ground.move(hero,0,-s)
            hY -= 1
            
    if event.keysym == 'Down'and hY != 5 :
            ground.move(hero,0,s)
            hY += 1
    if hX == fX and hY == fY:
        fX = randint(0,9)
        fY = randint(0,5)
        ground.coords(point,fX*128,fY*128)
        points += 1
        point1.config(text=points)
        if points>= win:
            mb.showinfo("you win",'congradulations')
            main.destroy()
            exit()
      

main = Tk()
main.title('Maze')
main.geometry('1280x896')
main.configure(bg='grey')

ground = Canvas(main, width=1280, height=768, bg='grey')
ground.pack(side = BOTTOM)
menu = Canvas(main, width=1280, height=896, bg='blue')
#ground.pack(side = BOTTOM)


shrine = PhotoImage(file = 's1.png')
heart = PhotoImage(file = 's2.png')
hand = PhotoImage(file = 's3.png')
skelet = PhotoImage(file = 's4.png')
bullet = PhotoImage(file = 's5.png')
#bgmenu =  PhotoImage(file = 's6.png')

#menu



#main canvas
lives= []
for q in range (hp):
    label1 = Label(main, image = heart, bg="grey")
    label1.pack(side = LEFT)
    lives.append(label1)

point1 = Label(main, text = points, bg = 'grey',fg = 'white', font = 'Impact 100' )
point1.pack(side = RIGHT)

fX = randint(0,9)
fY = randint(0,5)

hX = 0
hY = 0

enX = randint(0,9)
enY = randint(0,5) 

hero = ground.create_image(0, 0, image = skelet, anchor = 'nw')
point = ground.create_image(fX*s, fY*s, image = shrine, anchor = 'nw')

buL=[]

for k in range(4):
    obj = ground.create_image(enX*s, enY*s, image = bullet, anchor = 'nw')
    buL.append(obj)
en = ground.create_image(enX*s, enY*s, image = hand, anchor = 'nw')


main.bind('<KeyPress>',move)
vy()
main.mainloop()

