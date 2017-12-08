import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()
cameras=pygame.camera.list_cameras()
print (cameras[0])
cam = pygame.camera.Camera(cameras[0])
cam.start()
image = cam.get_image()
pygame.image.save(image,'temp.jpeg')
#_img = open('temp.jpeg','rb')
#_out = _img.read()
#_img.close()
