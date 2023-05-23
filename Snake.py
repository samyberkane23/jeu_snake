from tkinter import *
from random import randrange
import random
import time
from tkinter import ttk
fen = Tk()	
fen.title("Snake")
w = Canvas(fen, width=500, height=500, bg='black')
w.pack(side=TOP, padx=5, pady=5)

################################################################################################################
################################################################################################################
################################################################################################################

global direction_x
global direction_y
global dx
global dy
direction_x=0
direction_y=0
t  = True

global clic 
clic = 0

def gauche(event):
	global direction_x
	global direction_y
	if not (direction_x== 10 and direction_y == 0):
		direction_x=-10 
		direction_y =0
	
def droite(event):
	global direction_x
	global direction_y
	if not (direction_x== -10 and direction_y == 0):
		direction_x=10 
		direction_y =0
	
def haut(event):

	global direction_x
	global direction_y
	if not(direction_x == 0 and direction_y == 10):
		direction_x=0
		direction_y=-10
	
def bas(event):
	global direction_x
	global direction_y
	if not( direction_x== 0 and direction_y == -10):
		direction_x=0
		direction_y= 10

################################################################################################################
################################################################################################################
################################################################################################################

listNewObstacle=[]
def obstacle_alea():#fonction pour creer des obstacles aleatoirement 
	global obstacle
	ox = randrange(0, 49)
	oy= randrange(0, 49)
	ox=ox*10
	oy=oy*10
	obstacle=w.create_rectangle(ox,oy,ox+10,oy+10,fill='blue') #position des obstacles
	listNewObstacle.append(obstacle)

################################################################################################################
################################################################################################################
################################################################################################################

global score
score=0

#fonction qui fait bouger le serpent 
def bouger():

	global bouf
	global bx,by
	global obstacle
	global score
	global t

	if w.coords (snake[0])[2]>500 or w.coords (snake[0])[3]>500 or w.coords (snake[0])[0]<0 or w.coords (snake[0])[1]<0:#si il touche les extremites 
		texte = Label(fen, text = "PERDU", padx=5,pady=5)
		texte.pack()
		tex=Label(fen, text="votre score : "+str(score))
		tex.pack()
		return

	if w.coords (snake[0])[0] == w.coords (bouf)[0] and   w.coords (snake[0])[1] == w.coords (bouf)[1]:#si il touche la bouf en rouge 
		score=score+1
		x= randrange(0, 49)
		y= randrange(0, 49)
		w.delete(bouf)
		bouf =w.create_oval(x*10,y*10,(x+1)*10,(y+1)*10,fill='red')
		o = w.create_oval(w.coords (snake[len(snake)-1])[0],w.coords (snake[len(snake)-1])[1],w.coords (snake[len(snake)-1])[0]+10,w.coords (snake[len(snake)-1])[1]+10,fill='black')#cree un nouveau caree
		snake.append(o)
		obstacle_alea()

	for i in range(len(snake)-1):#faire bouger le serpent 
		w.move(snake[len(snake)-i-1],w.coords (snake[len(snake)-i-2])[0] - w.coords (snake[len(snake)-1-i])[0] ,w.coords (snake[len(snake)-i-2])[1] - w.coords (snake[len(snake)-i-1])[1])
	
	w.move(snake[0],direction_x,direction_y)#pour bouger la tete du serpent

	for i in range(len(listNewObstacle)):
		if w.coords (snake[0])[0] == w.coords (listNewObstacle[i])[0] and   w.coords (snake[0])[1] == w.coords (listNewObstacle[i])[1] :
			texte = Label(fen, text = "PERDU", padx=5,pady=5)
			texte.pack()
			tex=Label(fen, text="votre score : "+str(score))
			tex.pack()
			return
	#si le serpent ce mange 
	j=1
	while (j < len(snake)-1):

		if w.coords(snake[0])[0]== w.coords (snake[j])[0] and w.coords(snake[0])[1]== w.coords(snake[j])[1] and t :
			texte = Label(fen, text = "PERDU", padx=5,pady=5)
			texte.pack()
			tex=Label(fen, text="votre score : "+str(score))
			tex.pack()
			return
		j+=1

#changement de couleur pour serpent 
	i = 0
	for  i in range (len(snake)) :
		r=random.randint(0,255)
		g=random.randint(0,255)
		b=random.randint(0,255)
		w.itemconfig(snake[i],fill=f"#{r:02x}{g:02x}{b:02x}")
	
	if t :
		w.after(90,bouger)

		
################################################################################################################
################################################################################################################
################################################################################################################
def debut(): # fonction qui permet d'afficher un Toplevele pour choisir soit de : jouer , changer de la couleur du fond  ou de quitter le jeu
	top = Toplevel(fen)
	top.geometry("250x250+200+200")
	def jouer():
		top.destroy()
		bouger()
	
	def fond():

		def val(event):
			w['bg']=fond1.get()


		top1 = Toplevel(top)
		top1.geometry("180x180+250+250")
		img2=PhotoImage(file="image/image3.png")
		label2=Label(top1, image=img2)
		label2.pack()
		label2.image=img2
		fond1 = ttk.Combobox(top1, values=("black","dark slate gray","purple4", "navy", "snow4" , "dark green") )
		fond1.current(0)
		fond1.bind("<<ComboboxSelected>>",val)
		fond1.place(x=2, y=8) 	
		btn=Button(top1, text= '   Choisie  ' , bg='blue' , fg='black',command=top1.destroy)
		btn.place(x=50,y=80)

	img=PhotoImage(file="image/image.png")
	lable1=Label(top, image=img)
	lable1.pack()
	b= Button(top, text='    Jouer  ', bg='blue' , fg='black',command=jouer)
	b.place(x=90, y=10)
	b1= Button(top, text='   Fond   ', bg='blue' , fg='black', command=fond)
	b1.place(x=90, y=90)
	b2= Button(top, text='   Quitter', bg='blue' , fg='black', command=fen.destroy)
	b2.place(x=90, y=170)
	top.focus_set()
	top.grab_set()
	top.transient(fen)
	top.wait_window(fen)
	
################################################################################################################
################################################################################################################
################################################################################################################

snake=[]

serpent= w.create_oval(170,130,180,120,fill='black')#point de depart du serpent
snake.append(serpent)


bx = randrange(0, 49)
by= randrange(0, 49)
bx=bx*10
by=by*10

bouf =w.create_oval(bx,by,bx+10,by+10,fill='red')#la position de la bouf 


w.bind_all('<Left>',gauche)
w.bind_all('<Right>',droite)
w.bind_all('<Up>',haut)
w.bind_all('<Down>',bas)	



droite(0)
obstacle_alea()
debut()



fen.mainloop()



