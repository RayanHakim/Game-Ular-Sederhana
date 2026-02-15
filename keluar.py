import pygame
import config
import utils
import high_score 

def game_over_menu(score, difficulty, time_str):
    
    if high_score.check_is_high_score(difficulty, score) and score > 0:
        high_score.input_name_menu(score, difficulty, time_str)
    
    while True:
        config.dis.fill(config.BLACK)
        utils.draw_text_centered("GAME OVER", config.score_font, config.RED, config.dis, config.WIDTH/2, 80)
        utils.draw_text_centered(f"Skor: {score}", config.font_style, config.WHITE, config.dis, config.WIDTH/2, 130)
        utils.draw_text_centered(f"Waktu: {time_str}", config.info_font, config.WHITE, config.dis, config.WIDTH/2, 160)
        utils.draw_text_centered(f"Mode: {difficulty}", config.info_font, config.GREEN, config.dis, config.WIDTH/2, 190)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); quit()

        if utils.button("MAIN LAGI", 150, 250, 140, 50, config.GREEN, (100, 255, 100)): return 'restart'
        if utils.button("MENU", 310, 250, 140, 50, config.GRAY, config.WHITE): return 'menu'
        if utils.button("KELUAR", 230, 320, 140, 50, config.RED, (255, 100, 100)): 
            pygame.quit(); quit()

        pygame.display.update()
        config.clock.tick(15)