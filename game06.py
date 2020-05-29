import pygame
import random
import time
pygame.init()

# List of colors that can be used
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Load in outside sources
background = pygame.image.load('clouds.jpg')
plane_image = pygame.image.load('plane.png')
tower_image = pygame.image.load('tower.png')
heaven = pygame.image.load('heaven.jpg')
hell = pygame.image.load('hell.jpg')
song = pygame.mixer.music.load('song.wav')
death = pygame.mixer.Sound('death.wav')
pygame.mixer.music.play(-1)

# Screen size
dis_width = 600
dis_height = 400

# Name on top
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('9/11 Pilot Simulator')

# Keeps frame rate consistent
clock = pygame.time.Clock()

# Plane size and speed
tower = 10
plane = 10
plane_speed = 100

# Fonts for scoreboard and title
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Creates scoreboard
def Your_score(score):
    value = score_font.render("Towers hit: " + str(score), True, blue)
    dis.blit(value, [0, 0])

# Creates existence of plane
def our_plane(plane, plane_list):
    for x in plane_list:
        dis.blit(plane_image,[x[0], x[1], plane, plane])

def twin_tower(tower, tower_List):
    for x in tower_List:
        dis.blit(tower_image, [x[0], x[1][tower, tower]])

# Win game message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 20, dis_height / 3])

# Lose game message
def message2(msg, color):
    mesg2 = font_style.render(msg, True, color)
    dis.blit(mesg2, [dis_width / 20, dis_height - 50])

# Loops the game overtime
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    plane_List = []
    tower_List = []
    Length_of_plane = 1

# Randomly generates the tower on start
    border_height = dis_width - plane
    border_width = dis_height - plane
    towerx = round(random.randrange(0, border_height) / 10.0) * 10.0
    towery = round(random.randrange(0, border_width) / 10.0) * 10.0



    while not game_over:

        while game_close == True:

            # Message 1
            if x1 == (towerx + 10) and y1 == (towery + 60):
                dis.blit(heaven, (0,0))
                Your_score(1)
                message("You hit the tower and died for Allah! Good Job!", black)
                message2("Press Q to quit or C to do it again", black)

            # Message 2
            else:
                dis.blit(hell, (0,0))
                Your_score(0)
                message("You failed your mission! Try again or burn in hell!", black)
                message2("Press Q to quit or C to do it again", black)

            pygame.display.update()

            # Keys to end or continue the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Makes the movement keys work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -plane
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = plane
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -plane
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = plane
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
            death.play()

        x1 += x1_change
        y1 += y1_change
        # Puts New York in the background
        dis.blit(background, (0,0))

        # The tower placeholder for now
        if (towerx + 20 > border_width) and (towerx - 20 < 0) and (towery + 60 > border_height) and (towery - 60 < 0):
            return False
        if True:
            dis.blit(tower_image, [towerx, towery])
            pygame.display.update()

        # Puts the plane placeholder in the game
        plane_Head = []
        plane_Head.append(x1)
        plane_Head.append(y1)
        plane_List.append(plane_Head)
        if len(plane_List) > Length_of_plane:
            del plane_List[0]

        our_plane(plane, plane_List)
        twin_tower(tower, tower_List)
        Your_score(0)

        pygame.display.update()

        # Ends the game if tower and plane are at the same point
        if (x1) == (towerx + 10) and (y1) == (towery + 60):
            game_close = True
            if game_close == True:
                dis.fill(red)
                pygame.display.update()

        clock.tick(plane_speed)

    pygame.quit()
    quit()


gameLoop()
