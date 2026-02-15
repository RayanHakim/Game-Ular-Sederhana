import pygame
import config
import utils

def settings_menu():
    running = True
    
    while running:
        config.dis.fill(config.BLACK)
        utils.draw_text_centered("PENGATURAN", config.score_font, config.WHITE, config.dis, config.WIDTH/2, 40)
        
        # --- BAGIAN 1: KESULITAN (SPEED) ---
        status_text = "Normal"
        if config.current_speed == 10: status_text = "Mudah"
        elif config.current_speed == 25: status_text = "Sulit"
        
        utils.draw_text_centered(f"Kecepatan: {status_text}", config.font_style, config.YELLOW, config.dis, config.WIDTH/2, 90)

        # Tombol Kesulitan
        c_easy = config.WHITE if config.current_speed == 10 else config.GRAY
        c_norm = config.WHITE if config.current_speed == 15 else config.GRAY
        c_hard = config.WHITE if config.current_speed == 25 else config.GRAY

        if utils.button("Mudah", 100, 120, 100, 40, c_easy, config.WHITE): config.current_speed = 10
        if utils.button("Normal", 250, 120, 100, 40, c_norm, config.WHITE): config.current_speed = 15
        if utils.button("Sulit", 400, 120, 100, 40, c_hard, config.WHITE): config.current_speed = 25
        
        # --- BAGIAN 2: SKIN ULAR (COLOR) ---
        utils.draw_text_centered("Pilih Skin Ular:", config.font_style, config.YELLOW, config.dis, config.WIDTH/2, 190)
        
        # Preview Warna Aktif (Kotak Kecil di samping teks)
        pygame.draw.rect(config.dis, config.snake_color, [config.WIDTH/2 + 100, 175, 30, 30])
        pygame.draw.rect(config.dis, config.WHITE, [config.WIDTH/2 + 100, 175, 30, 30], 2) # Border

        # Tombol Pilihan Warna
        if utils.button("Biru", 70, 230, 80, 40, config.BLUE, config.LIGHT_GRAY): config.snake_color = config.BLUE
        if utils.button("Hijau", 160, 230, 80, 40, config.GREEN, config.LIGHT_GRAY): config.snake_color = config.GREEN
        if utils.button("Pink", 250, 230, 80, 40, config.MAGENTA, config.LIGHT_GRAY): config.snake_color = config.MAGENTA
        if utils.button("Cyan", 340, 230, 80, 40, config.CYAN, config.LIGHT_GRAY): config.snake_color = config.CYAN
        if utils.button("Oren", 430, 230, 80, 40, config.ORANGE, config.LIGHT_GRAY): config.snake_color = config.ORANGE

        # --- TOMBOL KEMBALI ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); quit()
        
        if utils.button("KEMBALI", 240, 320, 120, 50, config.RED, (255, 100, 100)):
            running = False 

        pygame.display.update()
        config.clock.tick(15)