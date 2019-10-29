from pygame.locals import *
import ctypes; ctypes.windll.user32.SetProcessDPIAware(); del ctypes

p.init()

fps = 60
clock = p.time.Clock()
width, height = 1920, 1080
surface = p.display.set_mode( (width, height), p.FULLSCREEN )
# surface = p.display.set_mode( (1000, 1000), )



event = []

app_loop = True
while app_loop:
	surface.fill( (255, 255, 255) )
	event = p.event.get()

	for e in event:
		if e.type == QUIT:
			app_loop = False
		elif e.type == KEYDOWN:
			if e.key == K_ESCAPE: app_loop = False



	p.display.flip()
	clock.tick( fps )
p.quit()
quit()