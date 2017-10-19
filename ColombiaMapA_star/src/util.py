'''
Utilities for Computer Vision, Howework 2
'''
from random import randint

#DUPLICADO :#/
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 0, 0)

# Set of colors in order to check status in the terminal
reset = '\x1b[0m'    # reset all colors to white on black
bold = '\x1b[1m'     # enable bold text
uline = '\x1b[4m'    # enable underlined text
nobold = '\x1b[22m'  # disable bold text
nouline = '\x1b[24m'  # disable underlined text
red = '\x1b[31m'     # red text
green = '\x1b[32m'   # green text
blue = '\x1b[34m'    # blue text
cyan = '\x1b[36m'    # cyan text
white = '\x1b[37m'   # white text (use reset unless it's only temporary)
yellow = '\x1b[33m'

warning = '{}[✘✘✘]{}'.format(red, reset)
info = '{}[!!!]{}'.format(yellow, reset)
ok = '{}[OK✓]{}'.format(cyan, reset)


version__ = '{}0.1v{}'.format(cyan, reset)
authors = '{}{}\tElvis Andrey, Sebastian, Héctor F.'.format(bold, red, reset)
#emails = '{}hfjimenez@utp.edu.co{}'.format(white, reset)
topic = '{}{}\n\t\tUTP:ArtificialInteligence 2017-2{}'.format(uline, white, reset)

l_art = [
    """{}
          ___           ___           ___         ___     
         /__/\         /  /\         /  /\       /  /\    
        |  |::\       /  /::\       /  /::\     /  /:/_   
        |  |:|:\     /  /:/\:\     /  /:/\:\   /  /:/ /\  
      __|__|:|\:\   /  /:/~/::\   /  /:/~/:/  /  /:/ /::\ {}
     /__/::::| \:\ /__/:/ /:/\:\ /__/:/ /:/  /__/:/ /:/\:\
    
     \  \:\~~\__\/ \  \:\/:/__\/ \  \:\/:/   \  \:\/:/~/:/
      \  \:\        \  \::/       \  \::/     \  \::/ /:/{} 
       \  \:\        \  \:\        \  \:\      \__\/ /:/  
        \  \:\        \  \:\        \  \:\       /__/:/   
         \__\/         \__\/         \__\/       \__\/{}
         """.format(yellow, blue, red, reset),        
]


def banner():
    art = l_art[randint(0, len(l_art) - 1)]
    print('{}\n{}, {}'.format(art, authors, topic))
