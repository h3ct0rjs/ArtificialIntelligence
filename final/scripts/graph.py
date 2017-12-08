import pygame
import label_image

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
pygame.init()
width=500
height=700
window=pygame.display.set_mode([width,height])
window.fill(white)
end=False

font=pygame.font.SysFont('Arial1',17,True,False)

if __name__== '__main__':
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end=True
    pygame.display.flip()