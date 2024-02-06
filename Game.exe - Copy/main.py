import pygame, sys, math
from pygame import mixer
pygame.init()

mixer.init()
#Load audio file
song1 = pygame.mixer.Sound('resources/image & sound/Menu_song.mp3')
pygame.mixer.music.load('resources/image & sound/Menu_song_offical.mp3')
song2 = pygame.mixer.Sound('resources/image & sound/Cut.mp3')
#Screen
screen = pygame.display.set_mode((1100,650))
icon = pygame.image.load("resources 2/Icon.png").convert_alpha()
pygame.display.set_caption("Game")
pygame.display.set_icon(icon)

bg_img = pygame.image.load("resources 2/Background.png")
bg_img = pygame.transform.scale(bg_img, (1100,650))

font_menu = pygame.image.load("resources 2/Font_menu.png")
font_menu = pygame.transform.scale(font_menu, (344,126))

play_button1 = pygame.image.load("resources 2/Play_button.png")
play_button1 = pygame.transform.scale(play_button1, (1100,65))
play_button2 = pygame.image.load("resources 2/Play_button2.png")
play_button2 = pygame.transform.scale(play_button2, (1100,65))
play_button = [play_button1,
               play_button2]

player = pygame.image.load("resources 2/Player.png")
player = pygame.transform.scale(player, (50,50))

text = pygame.image.load("resources 2/Text.png")

load = pygame.image.load("resources 2/Loading.png")

def loadandscale(i,size):
    a = pygame.image.load(i)
    a = pygame.transform.scale(a,size)
    return a

arrow = []
for i in range(1,6):
    arrow.append(loadandscale(f"resources 2/Arrow/{i}.png",(100,100)))
#image = []
#for i in range(1,10):
#    image.append(loadandscale(f"resources/image & sound/ezgif-frame-00{i}.jpg",(100,100)))
#for i in range(10,100):
#    image.append(loadandscale(f"resources/image & sound/ezgif-frame-0{i}.jpg",(100,100)))
#for i in range(100,201):
#    image.append(loadandscale(f"resources/image & sound/ezgif-frame-{i}.jpg",(100,100)))

#Game.exe/resources/image & sound/ezgif-frame-001.jpg

def game():
    #fadein
    x_player = 550
    y_player = 325
    x_player_change = 0
    y_player_change = 0
    
    second = 3
    delay_text = 6 * second
    y_text = 502
    y_text_change = 2
    animation_frame = 0
    animation_delay = 0.4
    player_rect = player.get_rect(center = (x_player,y_player))
    fadein = pygame.Surface((1100, 650))
    fadein = fadein.convert()
    fadein.fill('black')
    clock = pygame.time.Clock()
    tt = 1
    y_fm = 150
    time_y = 0
    y_pb = 400
    animation_image = 0
    animation_image_delay = 0.3
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            mousepos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == (pygame.K_w) or event.key == (pygame.K_UP):
                    y_player_change = -10
                if event.key == (pygame.K_s) or event.key == (pygame.K_DOWN):
                    y_player_change = 10
                if event.key == (pygame.K_d) or event.key == (pygame.K_RIGHT):
                    x_player_change = 10
                if event.key == (pygame.K_a) or event.key == (pygame.K_LEFT):
                    x_player_change = -10
                
        y_player_change *= 0.8
        x_player_change *= 0.8
        if not tt == 3:
            screen.blit(bg_img,(0,0))
        
        if tt == 1:
            mouse = pygame.mouse.get_pressed()
            play_rect = pygame.Rect(0,400,1100,65)
            screen.blit(font_menu, (370,y_fm))
            
            if play_rect.collidepoint(mousepos):
                screen.blit(play_button[1], (0,y_pb))
                if mouse[0]:
                    pygame.mixer.Sound.play(song2)
                    for i in range(255):
                        fadein.set_alpha(255-i)
                        screen.blit(fadein, (0, 0))
                        pygame.display.update()
                    pygame.mixer.Sound.play(song2)
                    tt = 2
            else:
                screen.blit(play_button[0], (0,y_pb))
                
            time_y += 10
            y_fm = (math.sin(time_y*10*12))*5 + 100
            y_pb = (math.sin(time_y*10*12))*5 + 400
        elif tt == 2:
            
            screen.blit(text,(0,y_text))
            screen.blit(arrow[animation_frame],(505,385))
            screen.blit(player, player_rect)
            player_rect = player.get_rect(center = (x_player,y_player))
            x_player += x_player_change
            y_player += y_player_change
            if x_player < 24:
                x_player_change = -3
                x_player = 24
                player_rect = player.get_rect(center = (x_player,y_player))
            if y_player > 612:
                y_player_change = 3
                y_player = 612
                player_rect = player.get_rect(center = (x_player,y_player))
            if y_player < 14:
                y_player_change = -3
                y_player = 14
                player_rect = player.get_rect(center = (x_player,y_player))
                
            if animation_frame == len(arrow)-1:
                animation_frame = 0
            if animation_delay < 0:
                animation_frame += 1
                animation_delay = 0.4
            animation_delay -= 0.1
            delay_text -= 0.1
            if delay_text < 0:
                y_text += y_text_change
                y_text_change += 1
                
            if x_player > 1150:
                pygame.mixer.Sound.play(song2)
                for i in range(255):
                    fadein.set_alpha(255-i)
                    screen.blit(fadein, (0, 0))
                    pygame.display.update()
                screen.blit(load,(320,285))
                pygame.display.update()
                x_player = 1000
                image = []
                for i in range(1,10):
                    image.append(loadandscale(f"resources/image & sound/ezgif-frame-00{i}.jpg",(1100,650)))
                for i in range(10,69):
                    image.append(loadandscale(f"resources/image & sound/ezgif-frame-0{i}.jpg",(1100,650)))
                print("music started playing....")

                #Set preferred volume
                mixer.music.set_volume(100)

                #Play the music
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(song1)
                
                tt = 3
                
                
        if tt == 3:
            if animation_image == len(image)-1:
                print("LOL")
                pygame.quit()
                sys.exit() 
            screen.blit(image[animation_image],(0,0))
            if animation_image_delay < 0:
                animation_image += 1
                animation_image_delay = 0.3
            animation_image_delay -= 0.1
            
            
            
        clock.tick(60)        
        pygame.display.update()
        
game()