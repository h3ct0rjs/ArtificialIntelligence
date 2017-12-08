import pygame
import keyboard
import pygame.camera
from pygame.locals import *
from scripts.label_image import *

blue=(0,0,255)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
pygame.init()
width=500
height=700
window=pygame.display.set_mode([width,height])
window.fill(white)
end=False
clock=pygame.time.Clock()

font=pygame.font.Font("fonts\pizza.ttf",25)

pygame.camera.init()
cameras=pygame.camera.list_cameras()
print (cameras[0])
cam = pygame.camera.Camera(cameras[0])
cam.start()
action=0
maximum=0
speed=0
image = cam.get_image()
time,label,result=core("temp.jpeg")

if __name__ == '__main__':

	while not end:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_KP5:				
					print ("Capture")
					pygame.image.save(image,'temp.jpeg')
					time,label,result=core("temp.jpeg")
					action=0
					maximum=0
		window.fill(white)


		image = cam.get_image()
		



		
		window.blit(image,(0,0))
		

		speed+=1
		xpos=50
		ypos=500
		counter=0
		for i in label:
			#print (i)
			window.blit(font.render(str(i)+" ",0,black),(xpos,ypos))
			ypos+=30
		ypos=500
		xpos+=100
		for i in result:
			action=float(i)
			if action>maximum:
				maximum=action
				flag=counter
			#print (i)
			i=float(i)*100
			window.blit(font.render(str(round(i,2))+" %",0,black),(xpos,ypos))
			ypos+=30
			counter+=1
		
		
		
		if speed>=3 and speed<7:
			keyboard.press('s')
		if speed>=7:
			keyboard.release('s')
			speed=0
		if flag==0: #fist
			keyboard.release('w+a')
			keyboard.release('s')
			keyboard.release('w+d')
			keyboard.press('w') 

			#print('Presiono arriba')
		if flag==1: #metal
			keyboard.release('w')
			keyboard.release('s')
			keyboard.release('w+d')
			keyboard.press('w+a')
			#print('Presiono izquierda')
		if flag==2: #paz
			keyboard.release('w+a')
			keyboard.release('s')
			keyboard.release('w')
			keyboard.press('w+d')
			#print('Presiono derecha')
		if flag==3: #stop
			keyboard.release('w+a')
			keyboard.release('w')
			keyboard.release('w+d')
			keyboard.press('s')
			#print('Presiono abajo')
		clock.tick(90)
		pygame.display.flip()  
