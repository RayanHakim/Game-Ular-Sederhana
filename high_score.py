import pygame
import json
import os
import config
import utils

DATA_FILE = "highscore.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        default_data = {"Mudah": [], "Normal": [], "Sulit": []}
        with open(DATA_FILE, "w") as f:
            json.dump(default_data, f)
        return default_data
    else:
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except:
            return {"Mudah": [], "Normal": [], "Sulit": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# UPDATE: Menambahkan parameter time_str
def add_high_score(difficulty, name, score, time_str):
    data = load_data()
    # Simpan nama, skor, DAN waktu
    data[difficulty].append({"name": name, "score": score, "time": time_str})
    data[difficulty].sort(key=lambda x: x["score"], reverse=True)
    data[difficulty] = data[difficulty][:5]
    save_data(data)

def check_is_high_score(difficulty, score):
    data = load_data()
    scores = data.get(difficulty, [])
    if len(scores) < 5: return True
    if score > scores[-1]["score"]: return True
    return False

def input_name_menu(score, difficulty, time_str):
    input_active = True
    user_text = ''
    
    while input_active:
        config.dis.fill(config.BLACK)
        utils.draw_text_centered("NEW HIGH SCORE!", config.score_font, config.GOLD, config.dis, config.WIDTH/2, 80)
        utils.draw_text_centered(f"Skor: {score} | Waktu: {time_str}", config.info_font, config.WHITE, config.dis, config.WIDTH/2, 130)
        utils.draw_text_centered(f"Mode: {difficulty}", config.info_font, config.GREEN, config.dis, config.WIDTH/2, 160)
        utils.draw_text_centered("Masukkan Nama:", config.font_style, config.WHITE, config.dis, config.WIDTH/2, 210)
        
        pygame.draw.rect(config.dis, config.WHITE, [config.WIDTH/2 - 100, 240, 200, 40], 2)
        
        text_surface = config.input_font.render(user_text, True, config.YELLOW)
        text_rect = text_surface.get_rect(center=(config.WIDTH/2, 260))
        config.dis.blit(text_surface, text_rect)

        utils.draw_text_centered("(Tekan ENTER)", config.info_font, config.GRAY, config.dis, config.WIDTH/2, 310)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(user_text) > 0: 
                        add_high_score(difficulty, user_text, score, time_str)
                        input_active = False 
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    if len(user_text) < 8:
                        user_text += event.unicode
        
        pygame.display.update()
        config.clock.tick(30)

def high_score_menu():
    hs_running = True
    selected_diff = "Normal"
    
    while hs_running:
        config.dis.fill(config.BLACK)
        utils.draw_text_centered("TOP 5 HIGH SCORES", config.score_font, config.GOLD, config.dis, config.WIDTH/2, 50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); quit()

        # Tombol Tab Difficulty
        btn_color_easy = config.GREEN if selected_diff == "Mudah" else config.GRAY
        btn_color_norm = config.YELLOW if selected_diff == "Normal" else config.GRAY
        btn_color_hard = config.RED if selected_diff == "Sulit" else config.GRAY
        
        if utils.button("Mudah", 50, 100, 100, 40, btn_color_easy, config.WHITE): selected_diff = "Mudah"
        if utils.button("Normal", 160, 100, 100, 40, btn_color_norm, config.WHITE): selected_diff = "Normal"
        if utils.button("Sulit", 270, 100, 100, 40, btn_color_hard, config.WHITE): selected_diff = "Sulit"

        data = load_data()
        scores = data.get(selected_diff, [])
        
        start_y = 160
        if not scores:
            utils.draw_text_centered("- Belum ada data -", config.font_style, config.GRAY, config.dis, config.WIDTH/2, 200)
        else:
            # UPDATE: Menampilkan Waktu juga
            for i, entry in enumerate(scores):
                # Ambil waktu, default "-" jika data lama belum ada waktu
                waktu = entry.get('time', '-') 
                text = f"{i+1}. {entry['name']} : {entry['score']} pts ({waktu})"
                utils.draw_text_centered(text, config.font_style, config.WHITE, config.dis, config.WIDTH/2, start_y + (i * 30))

        if utils.button("HAPUS", 450, 100, 100, 40, config.RED, (255, 100, 100)):
            if os.path.exists(DATA_FILE):
                os.remove(DATA_FILE)
            load_data() 

        if utils.button("KEMBALI", 240, 340, 120, 50, config.BLUE, (100, 100, 255)):
            hs_running = False

        pygame.display.update()
        config.clock.tick(15)