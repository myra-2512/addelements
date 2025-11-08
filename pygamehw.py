import pygame
rect=pygame.Rect(100,100,50,50)

def main():
    pygame.init()
    screen=pygame.display.set_mode((400,300))
    pygame.display.set_caption("Hello World")
    clock=pygame.time.Clock()
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(255,0,0),rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__=="__main__":
    main()