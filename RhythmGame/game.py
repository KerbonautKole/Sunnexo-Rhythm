import pygame
from datetime import datetime
pygame.init()

screen = pygame.display.set_mode((1000, 1000), pygame.SRCALPHA)
sunnexoImg = pygame.image.load("imgfiles/sunnexo.png")
sunnexoIcon  = pygame.image.load("imgfiles/sunnexo.png")
pygame.display.set_caption("Rhythm Game")
pygame.display.set_icon(sunnexoIcon)
sunnexo_45 = pygame.font.Font("fonts/sunnexo-45.otf", 20)
sunnexo_45_bold = pygame.font.Font("fonts/sunnexo-45-bold.otf", 20)
sunnexo_mono = pygame.font.Font("fonts/sunnexo-mono.ttf", 20)
ds_bios = pygame.font.Font("fonts/Nintendo-DS-BIOS.ttf", 30)
ds_bios_big = pygame.font.Font("fonts/Nintendo-DS-BIOS.ttf", 50)
heading = pygame.font.Font("fonts/sunnexo-45-bold.otf", 30)
subheading = pygame.font.Font("fonts/sunnexo-45.otf", 20)
background = pygame.image.load("imgfiles/ds_bios_hires.png")
font = pygame.font.Font(None, 50)
sunnexo_score_icon = pygame.transform.scale_by(sunnexoImg, 0.5)
button_dock_unscaled = pygame.image.load("imgfiles/dock.jpg")
button_dock = pygame.transform.scale_by(button_dock_unscaled, 3.5)
clock = pygame.time.Clock()
now = datetime.now()
month = now.month
day = now.day
pygame.mixer.music.load("Netpunk.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)




current_song = "Netpunk"
current_artist = "Sunnexo"
text_color = (100, 100, 100)
current_song_text = heading.render(current_song, True, (255, 255, 255))
current_artist_text = subheading.render(current_artist, True, (255, 255, 255))
sunnexo_scale = pygame.transform.scale(sunnexoImg, (30, 30))
sunnexo_45_test = sunnexo_45.render(("Sunnexo 45"), True, text_color)
sunnexo_45_bold_test = sunnexo_45_bold.render(("Sunnexo 45 Bold"), True, text_color)
sunnexo_mono_test = sunnexo_mono.render(("Sunnexo Mono"), True, text_color)
ds_bios_test = ds_bios.render(("Nintendo DS BIOS"), True, text_color)


top_bar_unscale = pygame.image.load("imgfiles/top_bar.jpg")
top_bar_width = top_bar_unscale.get_width()
top_bar_height = top_bar_unscale.get_height()
top_bar_width_target = 1000;
top_bar_scale = top_bar_width_target / top_bar_width
top_bar_height_target = int(top_bar_height * top_bar_scale)
top_bar = pygame.transform.scale(top_bar_unscale, (top_bar_width_target, top_bar_height_target))

score = 0
scoreText = font.render(("Score: " + str(score)), True, text_color)
state = 0
hit_text = ds_bios_big.render(("Hit!"), True, (0, 255, 0))
miss_text = ds_bios_big.render(("Miss!"), True, (255, 0, 0))
date_text = ds_bios_big.render((str(month) + "  " + str(day)), True, (255, 255, 255))
sunnexo_score_icon_y = 390

c1_mask = pygame.mask.from_surface(sunnexo_scale)
c2_mask = pygame.mask.from_surface(sunnexo_scale)
c3_mask = pygame.mask.from_surface(sunnexo_scale)
c4_mask = pygame.mask.from_surface(sunnexo_scale)

c1_state = False
c2_state = False
c3_state = False
c4_state = False

c1_color = (75, 9, 20)
c2_color = (89, 178, 172)
c3_color = (209, 31, 64)
c4_color = (19, 7, 36)
c1_color_alpha = (75, 9, 20, 128)
c2_color_alpha = (89, 178, 172, 128)
c3_color_alpha = (209, 31, 64, 128)
c4_color_alpha = (19, 7, 36, 128)
testCircleY = 100
testCircleLoc = (200, testCircleY)

c1_lane_surface = pygame.Surface((100, 700), pygame.SRCALPHA)
c2_lane_surface = pygame.Surface((100, 700), pygame.SRCALPHA)
c3_lane_surface = pygame.Surface((100, 700), pygame.SRCALPHA)
c4_lane_surface = pygame.Surface((100, 700), pygame.SRCALPHA)
pygame.draw.rect(c1_lane_surface, c1_color_alpha, (0, 0, 100, 700))
pygame.draw.rect(c2_lane_surface, c2_color_alpha, (0, 0, 100, 700))
pygame.draw.rect(c3_lane_surface, c3_color_alpha, (0, 0, 100, 700))
pygame.draw.rect(c4_lane_surface, c4_color_alpha, (0, 0, 100, 700))

c1_sunnexo = c1_mask.to_surface(setcolor = c1_color, unsetcolor = (0, 0, 0, 0))
c2_sunnexo = c1_mask.to_surface(setcolor = c2_color, unsetcolor = (0, 0, 0, 0))
c3_sunnexo = c1_mask.to_surface(setcolor = c3_color, unsetcolor = (0, 0, 0, 0))
c4_sunnexo = c1_mask.to_surface(setcolor = c4_color, unsetcolor = (0, 0, 0, 0))


c1_letter = font.render("a", True, (255, 255, 255))
c1_letter_rect = c1_letter.get_rect()
c1_letter_rect.center = (200, 750)

c2_letter = font.render("s", True, (255, 255, 255))
c2_letter_rect = c1_letter.get_rect()
c2_letter_rect.center = (400, 750)

c3_letter = font.render("k", True, (255, 255, 255))
c3_letter_rect = c1_letter.get_rect()
c3_letter_rect.center = (600, 750)

c4_letter = font.render("l", True, (255, 255, 255))
c4_letter_rect = c1_letter.get_rect()
c4_letter_rect.center = (804, 750)

running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(c1_lane_surface, (150, 45))
    screen.blit(c2_lane_surface, (350, 45))
    screen.blit(c3_lane_surface, (550, 45))
    screen.blit(c4_lane_surface, (750, 45))
    screen.blit(top_bar, (0, 0))
    screen.blit(current_song_text, (10, 10))
    screen.blit(current_artist_text, (225, 20))
    screen.blit(date_text, (745, 5))
    screen.blit(button_dock, (131.25, 668.75))

    if state == 1:
        screen.blit(hit_text, (640, 5))
    elif state == 2:
        screen.blit(miss_text, (640, 5))
    for event in pygame.event.get():

        #quit
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                c1_state = True
            if event.key == pygame.K_s:
                c2_state = True
            if event.key == pygame.K_k:
                c3_state = True
            if event.key == pygame.K_l:
                c4_state = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                c1_state = False
            if event.key == pygame.K_s:
                c2_state = False
            if event.key == pygame.K_k:
                c3_state = False
            if event.key == pygame.K_l:
                c4_state = False

    if 740 <= testCircleY <= 760:
        if c1_state == True:
            score += 1
            testCircleY = 100
            state = 1
            sunnexo_score_icon_y -= 1
    if testCircleY > 760:
        state = 2
        score -= 1
        sunnexo_score_icon_y += 1
        testCircleY = 100;



    pygame.draw.circle(screen, c1_color, (200, 750), 55)
    pygame.draw.circle(screen, c2_color, (400, 750), 55)
    pygame.draw.circle(screen, c3_color, (600, 750), 55)
    pygame.draw.circle(screen, c4_color, (800, 750), 55)

    #1st
    if c1_state == True:
        pygame.draw.circle(screen, c1_color, (200, 750), 50)
        pygame.draw.circle(screen, (255, 255, 255), (200, 750), 25)
        screen.blit(c1_sunnexo, (185, 735))
    elif c1_state == False:
        pygame.draw.circle(screen, (255, 255, 255), (200, 750), 50)
        pygame.draw.circle(screen, c1_color, (200, 750), 25)
        screen.blit(c1_letter, c1_letter_rect)

    # 2nd
    if c2_state == True:
        pygame.draw.circle(screen, c2_color, (400, 750), 50)
        pygame.draw.circle(screen, (255, 255, 255), (400, 750), 25)
        screen.blit(c2_sunnexo, (385, 735))
    elif c2_state == False:
        pygame.draw.circle(screen, (255, 255, 255), (400, 750), 50)
        pygame.draw.circle(screen, c2_color, (400, 750), 25)
        screen.blit(c2_letter, c2_letter_rect)

    # 3rd
    if c3_state == True:
        pygame.draw.circle(screen, c3_color, (600, 750), 50)
        pygame.draw.circle(screen, (255, 255, 255), (600, 750), 25)
        screen.blit(c3_sunnexo, (585, 735))
    elif c3_state == False:
        pygame.draw.circle(screen, (255, 255, 255), (600, 750), 50)
        pygame.draw.circle(screen, c3_color, (600, 750), 25)
        screen.blit(c3_letter, c3_letter_rect)

    # 4th
    if c4_state == True:
        pygame.draw.circle(screen, c4_color, (800, 750), 50)
        pygame.draw.circle(screen, (255, 255, 255), (800, 750), 25)
        screen.blit(c4_sunnexo, (785, 735))
    elif c4_state == False:
        pygame.draw.circle(screen, (255, 255, 255), (800, 750), 50)
        pygame.draw.circle(screen, c4_color, (800, 750), 25)
        screen.blit(c4_letter, c4_letter_rect)






    pygame.draw.circle(screen, c1_color, testCircleLoc, 55)
    pygame.draw.circle(screen, (255, 255, 255), testCircleLoc, 50)
    testCircleY += 5
    testCircleLoc = (200, testCircleY)
    scoreText = sunnexo_mono.render(("Score: " + str(score)), True, text_color)
    screen.blit(scoreText, (131, 838))
    screen.blit(sunnexo_45_test, (0, 980))
    screen.blit(sunnexo_45_bold_test, (200, 980))
    screen.blit(sunnexo_mono_test, (490, 980))
    screen.blit(ds_bios_test, (735, 980))
    pygame.draw.line(screen, c2_color, (70, 100), (70, 250), width=10)
    pygame.draw.line(screen, c3_color, (70, 250), (70, 400), width=10)
    pygame.draw.line(screen, c1_color, (70, 400), (70, 550), width=10)
    pygame.draw.line(screen, c4_color, (70, 550), (70, 700), width=10)

    screen.blit(sunnexo_score_icon, (40, sunnexo_score_icon_y))
    pygame.display.flip()
    clock.tick(60)