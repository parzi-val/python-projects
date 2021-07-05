from tkinter import *  # noqa: F403
from tkinter import messagebox
import pygame
import random

# snake game ->


def game():
    root.withdraw()
    pygame.init()

    display = pygame.display.set_mode((800, 600))

    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (135, 206, 250)

    display_width = 800
    display_height = 600

    msg_font = pygame.font.SysFont("consolas", 25)
    score_font = pygame.font.SysFont("consolas", 35)

    block = 10
    snake_speed = int(a)

    def score_snake(score):
        value = score_font.render("Score: " + str(score), True, white)
        display.blit(value, [335, 0])

    def message(msg, color):
        message_ = msg_font.render(msg, True, color)
        display.blit(message_, [100, 280])

    clock = pygame.time.Clock()

    def snake(snake_list, block):
        for x in snake_list:
            pygame.draw.rect(display, green, [x[0], x[1], block, block])

    def gameloop():

        x1 = display_width / 2
        y1 = display_height / 2

        x1_change = 0
        y1_change = 0

        gameover = False
        gameclose = False

        x2 = round(random.randrange(0, display_width - block) / 10.0) * 10.0
        y2 = round(random.randrange(0, display_height - block) / 10.0) * 10.0

        snake_list = []
        length_snake = 1
        while not gameover:

            while gameclose is True:
                message("You lost! enter -> play again , esc -> quit ", white)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            gameover = True
                            gameclose = False
                            root.deiconify()
                        if event.key == pygame.K_RETURN:
                            gameloop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = True
                    root.deiconify()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        x1_change = -10
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        x1_change = 10
                        y1_change = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        y1_change = -10
                        x1_change = 0
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        y1_change = 10
                        x1_change = 0
            if h is True:
                if x1 >= display_width:
                    x1 = 0
                elif x1 <= 0:
                    x1 = display_width
                elif y1 >= display_height:
                    y1 = 0
                elif y1 <= 0:
                    y1 = display_height
            elif h is False:
                if x1 >= display_width or x1 <= 0 or y1 >= display_height or y1 <= 0:
                    gameclose = True

            x1 += x1_change
            y1 += y1_change
            display.fill(black)

            pygame.draw.rect(display, blue, [x2, y2, block, block])
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > length_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    gameclose = True
            snake(snake_list, block)
            score_snake(length_snake - 1)
            pygame.display.update()

            if x1 == x2 and y1 == y2:
                x2 = round(random.randrange(0, display_width - 50) / 10.0) * 10.0
                y2 = round(random.randrange(0, display_height - 50) / 10.0) * 10.0
                length_snake += 1
            clock.tick(snake_speed)

        pygame.quit()

    gameloop()


# ...

# gui ->

a = 30


def difficulty():
    global a
    a = var.get()
    if a == 1:
        a = 10
    elif a == 2:
        a = 20
    elif a == 3:
        a = 30
    elif a == 4:
        a = 40
    elif a == 5:
        a = 50


def rules():
    messagebox.showinfo(
        "RULES",
        "‣ Use WASD or arrow keys to navigate \n‣ If the snake hits the edges of the box the game will be over \n‣The game will be over if the snake collides with itself",
    )


h = False


def hard():
    global h
    if h is False:
        h = True
        difh.config(text="HARD")
    elif h is True:
        h = False
        difh.config(text="EASY")


root = Tk()
root.title("python")
root.geometry("400x400")
root.configure(bg="gray15")

frame = Frame(root, bg="black", bd=5, relief=RIDGE)
frame.place(x=100, y=110)


label = Label(root, font=("Courier", 30, "bold"), bg="gray15", fg="white", bd=30)
label.config(text="python")
label.place(x=100, y=3)

var = DoubleVar()

start = Button(frame, text="PLAY", command=game)
dif = Scale(
    frame,
    variable=var,
    orient=HORIZONTAL,
    from_=1,
    to=5,
    length=200,
    bg="white",
    troughcolor="black",
)
difb = Button(frame, text="SET DIFFICULTY", command=difficulty)
difh = Button(frame, text="EASY", command=hard)
rules = Button(frame, text="RULES", command=rules)
l1 = Label(frame, bg="black")
l2 = Label(frame, bg="black")
l3 = Label(frame, bg="black")
l4 = Label(frame, bg="black")

start.pack()
l1.pack()
dif.pack()
dif.set(3)
l2.pack()
difb.pack()
l3.pack()
difh.pack()
l4.pack()
rules.pack()


root.mainloop()
# ...
