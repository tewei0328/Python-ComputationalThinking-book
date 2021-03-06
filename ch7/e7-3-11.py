#e7-3-11彈跳球遊戲
import pygame, sys
pygame.init() #load pygame modules
size = width, height = 400, 300 #size of window
speed = [2, 2] #speed and direction
screen = pygame.display.set_mode(size) #make window
s=pygame.Surface((100,50)) #create surface 100px by 50px
s.fill((33,66,99)) #color the surface blue
r=s.get_rect() #get the rectangle bounds for the surface
clock=pygame.time.Clock() #make a clock
while 1: #infinite loop
        clock.tick(30) #limit framerate to 30 FPS
        for event in pygame.event.get(): #if something clicked
                if event.type == pygame.QUIT: #if EXIT clicked
                        sys.exit() #close cleanly
        r=r.move(speed) #move the box by the "speed" coordinates
        #if we hit a  wall, change direction
        if r.left < 0 or r.right > width: speed[0] = -speed[0]
        if r.top < 0 or r.bottom > height: speed[1] = -speed[1]
        screen.fill((0,0,0)) #make redraw background black
        screen.blit(s,r) #render the surface into the rectangle
        pygame.display.flip() #update the screen





