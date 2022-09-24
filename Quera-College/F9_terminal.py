import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("test window")

wi = (255, 255, 255)
size = 1
color = (0, 0, 0)
screen.fill(wi)
pygame.display.update()
while True:
    intput = input()

    if intput == "end drawing":
        pygame.event.pump()
        pygame.image.save(screen, 'draw.png')
        break

    elif intput.find("size") != -1:
        size = int(intput.replace("change size ", ""))

    elif intput.find("color") != -1:
        x = intput.replace("change color ", "").replace(" ", ",")
        for i in range(len(x.split(","))):
            y = list(color)
            y[i] = int(x.split(",")[i])
            color = tuple(y)

    elif intput.find("line") != -1:
        x = intput.replace("draw line ", "").replace(" ", ",")
        for i in range(len(x.split(","))):
            pygame.draw.line(screen, color, (int(x.split(",")[0]), int(x.split(",")[1])),
                             (int(x.split(",")[2]), int(x.split(",")[3])), size)
        pygame.display.update()

    elif intput.find("circle") != -1:
        x = intput.replace("draw circle ", "").replace(" ", ",")
        for i in range(len(x.split(","))):
            pygame.draw.circle(screen, color, (float(x.split(",")[0]), float(x.split(",")[1])), (int(x.split(",")[2])),
                               size)
        pygame.display.update()

    elif intput.find("polygon") != -1:
        x = intput.replace("draw polygon ", "").replace(" ", ",")
        for i in range(len(x.split(","))):
            pygame.draw.polygon(screen, color, [(float(x.split(",")[0]), float(x.split(",")[1])),
                                                (float(x.split(",")[2]), float(x.split(",")[3])),
                                                (float(x.split(",")[4]), float(x.split(",")[5])),
                                                (float(x.split(",")[6]), float(x.split(",")[7]))], size)
        pygame.display.update()

# draw line 100 150 200 150
# draw line 150 100 150 200
# change color 255 0 0
# change size 2
# draw circle 150 150 50
# end drawing
