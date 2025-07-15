# Import necessary libraries
import pygame
import random
import pygame_widgets 
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


rec1_resize_start = None
rec2_resize_start = None
resize_duration = 5000  # 3 seconds

# Initialize pygame nad mixer
pygame.mixer.init()
pygame.init()

# menu image
menu_image = pygame.image.load(resource_path("pong.png"))
menu_image = pygame.transform.scale(menu_image, (225, 225))
icon = pygame.image.load(resource_path('pong_display.png'))
pygame.display.set_icon(icon)


# Load sounds
hit_sound = pygame.mixer.Sound(resource_path("ponghit.wav"))
point_sound = pygame.mixer.Sound(resource_path("point_scored.mp3"))
power_up = pygame.mixer.Sound(resource_path("powerup.mp3"))
win = pygame.mixer.Sound(resource_path("win.mp3"))
button = pygame.mixer.Sound(resource_path("button.mp3"))

# Set up display
pygame.display.set_caption("Pong Game")
screen = pygame.display.set_mode((800, 600))

# Set up clock
clock = pygame.time.Clock()

# Colors
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
light_grey  = (255, 255, 255)

# Fonts
font = pygame.font.Font(None, 100)
pong_font = pygame.font.Font(resource_path("russo.ttf"), 80)
winner_font = pygame.font.Font(resource_path("russo.ttf"), 80)
result_font = pygame.font.Font(resource_path("russo.ttf"), 30)

# Game state
game_state = "menu"
winner_text = ""
vs_computer = False

# Scores
scores = [0, 0]

# Paddle setup
rec1 = pygame.Rect(50, 250, 20, 100)
rec2 = pygame.Rect(730, 250, 20, 100)
rec1_speed = 6
rec2_speed = 6

# Ball setup
BALL_INTIAL_VEL = [8, 3]
ball_pos = [400, 300]
ball_vel = [8, 3]
scored = False

# Slider
speed_slider = Slider(screen, 350, 360, 250, 15, min=4, max=15, step=1)
speed_display = TextBox(screen, 600, 350, 50, 30, fontSize=18)
speed_display.disable()

# Power-up 1
pu_pos = [400, random.choice([100, 500])]
pu_vel = [5, 0]
throw_rand = [random.randint(0, 4)]
rand_operation_choice = ["+", "-"]
rand_operation = random.choice(rand_operation_choice)

# Power-up 2
pu2_pos = [400, random.choice([100, 500])]
pu2_vel = [5, 0]
throw_rand2 = [random.randint(0, 4)]
rand_operation_choice2 = ["+", "-"]
rand_operation2 = random.choice(rand_operation_choice2)

# Button class
class Button:
    def __init__(self, x, y, width, height, text, command):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.command = command

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.command()

def start_game():
    global game_state, scores, ball_pos, ball_vel, rec1, rec2, scored, button
    button.play()
    game_state = "play"
    scores = [0, 0]
    ball_pos[:] = [400, 300]
    x_speed = speed_slider.getValue()
    y_speed = random.choice([-3, 3])
    ball_vel[:] = [x_speed, y_speed]
    rec1.y = 250
    rec2.y = 250
    scored = False

    speed_slider.hide()
    speed_display.hide()

def reset_game():
    global game_state, scores, ball_pos, ball_vel, rec1, rec2, scored
    global pu_pos, pu2_pos, pu_vel, pu2_vel, rec1_resize_start, rec2_resize_start
    global rand_operation, rand_operation2, throw_rand, throw_rand2, button
    button.play()
    game_state = "menu"
    scores = [0, 0]
    ball_pos[:] = [400, 300]
    ball_vel[:] = BALL_INTIAL_VEL[:]
    rec1.y = 250
    rec2.y = 250
    scored = False
    pu_pos = [400, random.choice([100, 500])]
    pu2_pos = [400, random.choice([100, 500])]
    pu_vel = [5, 0]
    pu2_vel = [5, 0]

    throw_rand = [random.randint(0, 4)]
    throw_rand2 = [random.randint(0, 4)]

    rand_operation = random.choice(rand_operation_choice)
    rand_operation2 = random.choice(rand_operation_choice2)

    speed_slider.show()
    speed_display.show()

def enable_computer():
    global vs_computer, game_state, button
    button.play()
    vs_computer = True
    start_game()

# Object buttons
play_button = Button(275, 425, 250, 50, "Play with a friend", start_game)
reset_button = Button(350, 500, 100, 50, "Reset", reset_game)
computer_button = Button(275, 500, 250, 50, "Play with Computer", enable_computer )


running = True
while running:
    clock.tick(60)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "menu":
            play_button.handle_event(event)
            computer_button.handle_event(event)
        elif game_state == "game_over":
            reset_button.handle_event(event)

    screen.fill(light_grey)

    if game_state == "menu":
        screen.blit(menu_image, (300, 15))
        play_button.draw(screen)
        computer_button.draw(screen)
        text_pong = pong_font.render("Pong Game", True, black)
        screen.blit(text_pong, (200, 250))
        speed_label = result_font.render("Ball Speed:", True, black)
        screen.blit(speed_label, (150, 350))
        speed_display.setText(str(speed_slider.getValue()))

    elif game_state == "play":

        # Draw the midleine
        pygame.draw.line(screen, black, (400, 0), (400, 600), 5)

        # Draw scores
        text = font.render(f"{scores[0]}                  {scores[1]}", True, black)
        screen.blit(text, (200, 10))

        # Draw paddles
        pygame.draw.rect(screen, red, rec1, )
        pygame.draw.rect(screen, black, rec1, width=8)
        pygame.draw.rect(screen, blue, rec2, )
        pygame.draw.rect(screen, black, rec2, width=8)

        # Paddle movement
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            rec1.y -= rec1_speed
        if key[pygame.K_s]:
            rec1.y += rec1_speed

        if vs_computer:
         rec2_speed = 3
         if abs(rec2.centery - ball_pos[1]):

          if rec2.centery < ball_pos[1]:
           rec2.y += rec2_speed
          elif rec2.centery > ball_pos[1]:
           rec2.y -= rec2_speed
        else:
          if key[pygame.K_UP]:
            rec2.y -= rec2_speed
          if key[pygame.K_DOWN]:
            rec2.y += rec2_speed


        # Keep paddles on screen
        rec1.y = max(0, min(rec1.y, 600 - rec1.height))
        rec2.y = max(0, min(rec2.y, 600 - rec2.height))

        # Draw ball
        ball = pygame.draw.circle(screen, white, (int(ball_pos[0]), int(ball_pos[1])), 15, )
        pygame.draw.circle(screen, black, (int(ball_pos[0]), int(ball_pos[1])), 15, width=8)

        # Ball movement
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        if scores[0] == throw_rand[0] or scores[1] == throw_rand[0]:

         # Draw power-up
         pu = pygame.draw.circle(screen, (0, 255, 0), (int(pu_pos[0]), int(pu_pos[1])), 10)

         # power-up movement
         if rand_operation == "+":
             pu_pos[0] += pu_vel[0]
         elif rand_operation == "-":
             pu_pos[0] -= pu_vel[0]

         # Larging the paddles if they collide with the power-up
         if pu.colliderect(rec1) or pu.colliderect(rec2):
             if pu.colliderect(rec1):
                 power_up.play()
                 rec1.height = 200
                 rec1_resize_start = pygame.time.get_ticks()
                 pu = None  # Move power-up off screen

             else:
                 power_up.play()
                 rec2.height = 200
                 rec2_resize_start = pygame.time.get_ticks()
                 pu = None
        
         current_time = pygame.time.get_ticks()

         if rec1_resize_start and current_time - rec1_resize_start >= resize_duration:
           rec1.height = 100
           rec1_resize_start = None

         if rec2_resize_start and current_time - rec2_resize_start >= resize_duration:
           rec2.height = 100
           rec2_resize_start = None

        # Draw second power-up
        if scores[0] == throw_rand2[0] or scores[1] == throw_rand2[0]:
        
         pu2 = pygame.draw.circle(screen, (0, 255, 0), (int(pu2_pos[0]), int(pu2_pos[1])), 10)

         # power-up2 movement
         if rand_operation2 == "+":
             pu2_pos[0] += pu2_vel[0]
         elif rand_operation2 == "-":
             pu2_pos[0] -= pu2_vel[0]

         # Larging the paddles if they collide with the power-up2
         if pu2.colliderect(rec1) or pu2.colliderect(rec2):
             if pu2.colliderect(rec1):
                 power_up.play()
                 rec1.height = 200
                 rec1_resize_start = pygame.time.get_ticks()
                 pu2 = None  # Move power-up off screen

             else:
                 power_up.play()
                 rec2.height = 200
                 rec2_resize_start = pygame.time.get_ticks()
                 pu2 = None
        
         current_time = pygame.time.get_ticks()

         if rec1_resize_start and current_time - rec1_resize_start >= resize_duration:
           rec1.height = 100
           rec1_resize_start = None

         if rec2_resize_start and current_time - rec2_resize_start >= resize_duration:
           rec2.height = 100
           rec2_resize_start = None
          

        # Ball collision with paddles
        if ball.colliderect(rec1) or ball.colliderect(rec2):
            if ball.colliderect(rec1):
                ball_vel[0] = abs(ball_vel[0])
            else:
                ball_vel[0] = -abs(ball_vel[0])

        # Ball collision with top/bottom
        if ball_pos[1] - 15 <= 0 or ball_pos[1] + 15 >= 600:
            ball_vel[1] = -ball_vel[1]

        # Adding ball collision sound
        if ball.colliderect(rec1) or ball.colliderect(rec2) or ball_pos[1] - 15 <= 0 or ball_pos[1] + 15 >= 600:
            hit_sound.play()

        # Adding the point scored sound
        if ball_pos[0] <= 0 or ball_pos[0] >= 800:
            point_sound.play()

        # Scoring
        if not scored:
            if ball_pos[0] <= 0:
                scores[1] += 1
                scored = True
            elif ball_pos[0] >= 800:
                scores[0] += 1
                scored = True

        # Reset after score
        if scored:
            ball_pos[:] = [400, 300]
            x_speed = speed_slider.getValue() 
            ball_vel[:] = [x_speed, random.choice([-3, 3])]
            rec1.y = 250
            rec2.y = 250
            scored = False

        # Check for winner
        if scores[0] == 5 or scores[1] == 5:
            win.play()
            winner_text = "Player 1 Wins!" if scores[0] == 5 else "Player 2 Wins!" 
            game_state = "game_over"

    elif game_state == "game_over":
        screen.fill(white)
        winner_pong = winner_font.render(winner_text, True, black)
        screen.blit(winner_pong, (150, 100))
        play1_score_text = result_font.render(f"Player 1 Score: {scores[0]}", True, black)
        play2_score_text = result_font.render(f"Player 2 Score: {scores[1]}", True, black)
        screen.blit(play1_score_text, (300, 300))
        screen.blit(play2_score_text, (300, 350))

        reset_button.draw(screen)
        
    pygame_widgets.update(pygame.event.get())
    pygame.display.flip()

pygame.quit()
