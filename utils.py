import pygame
import time
import config 

def draw_text_centered(text, font, color, surface, center_x, center_y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(center=(center_x, center_y))
    surface.blit(textobj, textrect)

def button(msg, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    action_triggered = False

    # Cek Hover
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(config.dis, ac, (x, y, w, h)) 
        if click[0] == 1:
            while pygame.mouse.get_pressed()[0]:
                pygame.event.pump() 
            action_triggered = True
    else:
        pygame.draw.rect(config.dis, ic, (x, y, w, h)) 

    text_surf = config.button_font.render(msg, True, config.BLACK)
    text_rect = text_surf.get_rect(center=(x + (w / 2), y + (h / 2)))
    config.dis.blit(text_surf, text_rect)
    
    return action_triggered

def show_hud(score, elapsed_time, difficulty):
    # Skor
    value = config.info_font.render("Skor: " + str(score), True, config.YELLOW)
    config.dis.blit(value, [10, 10])
    
    # Timer
    mins = int(elapsed_time // 60)
    secs = int(elapsed_time % 60)
    timer_text = f"Waktu: {mins:02d}:{secs:02d}"
    timer_surface = config.info_font.render(timer_text, True, config.WHITE)
    config.dis.blit(timer_surface, [config.WIDTH/2 - 50, 10])

    # Mode
    mode_text = f"Mode: {difficulty}"
    mode_surface = config.info_font.render(mode_text, True, config.GREEN)
    config.dis.blit(mode_surface, [config.WIDTH - 120, 10])