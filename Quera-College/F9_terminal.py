import pygame

from math import pi


draw line 100 150 200 150
draw line 150 100 150 200
change color 255 0 0
change size 2
draw circle 150 150 50
end drawing


pygame.init()

screen = pygame.display.set_mode((800, 600))

red = (252.2, 0, 0)

blue = (0, 0, 255)

amber = (100, 75, 0)

aqua = (0, 100, 100)

bittersweet = (100, 44, 37)

green = (0, 255, 0)

aero_blue = (75, 91, 84)

gray = (128, 128, 128)

screen.fill(gray)

pygame.draw.line(screen, red, (300.4, 300), (600, 400), 10)

pygame.draw.circle(screen, amber, (200, 200), 20, 6)

pygame.draw.rect(screen, blue, (400, 400, 30, 80), 20)

pygame.draw.ellipse(screen, aqua, (450, 450, 100, 50), 10)

pygame.draw.polygon(screen, bittersweet, [(700, 500), (600, 500), (550, 450), (650, 440)], 10)

pygame.draw.lines(screen, green, True, [(700, 200), (600, 200), (550, 150), (650, 140)], 20)

pygame.draw.lines(screen, green, False, [(700, 350), (600, 350), (550, 300), (650, 290)], 30)

pygame.draw.arc(screen, aero_blue,  (210, 75, 150, 125), 3*pi/2, 2*pi, 25)

pygame.display.update()

while True:

    pygame.event.pump()