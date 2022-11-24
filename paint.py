import pygame


def paint():
    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (135, 206, 250)

    isPressed = False

    screen = pygame.display.set_mode((500, 500))

    def drawCircle(screen, x, y):
        pygame.draw.circle(screen, white, (x, y), 5)

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
            if event.type == pygame.MOUSEMOTION and isPressed is True:
                (x, y) = pygame.mouse.get_pos()
                drawCircle(screen, x, y)
        pygame.display.flip()


paint()
