import pygame
import time
import random
import config
import utils
import setting
import high_score
import keluar

# --- FUNGSI BANTUAN ---
def get_random_position(snake_list):
    while True:
        x = round(random.randrange(0, config.WIDTH - config.SNAKE_BLOCK) / 10.0) * 10.0
        y = round(random.randrange(0, config.HEIGHT - config.SNAKE_BLOCK) / 10.0) * 10.0
        
        conflict = False
        for block in snake_list:
            if block[0] == x and block[1] == y:
                conflict = True
                break
        
        if not conflict:
            return x, y

def draw_grid():
    for x in range(0, config.WIDTH, config.SNAKE_BLOCK):
        pygame.draw.line(config.dis, (40, 40, 40), (x, 0), (x, config.HEIGHT))
    for y in range(0, config.HEIGHT, config.SNAKE_BLOCK):
        pygame.draw.line(config.dis, (40, 40, 40), (0, y), (config.WIDTH, y))

def pause_menu(start_pause_time):
    paused = True
    action = 'resume'

    while paused:
        pygame.draw.rect(config.dis, config.BLUE, [150, 50, 300, 300])
        pygame.draw.rect(config.dis, config.WHITE, [150, 50, 300, 300], 2)
        utils.draw_text_centered("GAME PAUSED", config.score_font, config.WHITE, config.dis, config.WIDTH/2, 90)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False

        if utils.button("LANJUT", 200, 150, 200, 40, config.GREEN, config.LIGHT_GRAY):
            paused = False
            action = 'resume'
        if utils.button("RESTART", 200, 200, 200, 40, config.YELLOW, config.LIGHT_GRAY):
            paused = False
            action = 'restart'
        if utils.button("MENU UTAMA", 200, 250, 200, 40, config.GRAY, config.LIGHT_GRAY):
            paused = False
            action = 'menu'

        pygame.display.update()
        config.clock.tick(15)
    
    end_pause_time = time.time()
    return (end_pause_time - start_pause_time), action

def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        pygame.draw.rect(config.dis, config.snake_color, [x[0], x[1], snake_block, snake_block])
        
        # Mata Ular (Kepala)
        if i == len(snake_list) - 1:
            head_x = x[0]
            head_y = x[1]
            pygame.draw.circle(config.dis, config.WHITE, (int(head_x + 3), int(head_y + 3)), 2)
            pygame.draw.circle(config.dis, config.WHITE, (int(head_x + 7), int(head_y + 3)), 2)

def gameLoop():
    game_over = False
    stop_game_completely = False 
    
    x1 = config.WIDTH / 2
    y1 = config.HEIGHT / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    current_score = 0 

    data = high_score.load_data()
    diff_str = "Normal"
    if config.current_speed == 10: diff_str = "Mudah"
    elif config.current_speed == 25: diff_str = "Sulit"
    
    top_score = 0
    if len(data[diff_str]) > 0:
        top_score = data[diff_str][0]['score']

    foodx, foody = get_random_position([]) 

    poison_active = False
    poison_x = -100
    poison_y = -100
    poison_start_time = 0
    poison_duration = 10     
    poison_interval = 15     
    last_poison_spawn = time.time() 

    bonus_food_active = False
    bonus_size = 20 
    bonus_x = -100
    bonus_y = -100
    bonus_start_time = 0
    bonus_duration = 10 
    next_bonus_spawn_time = 30 

    start_time = time.time()
    total_pause_duration = 0

    while not game_over and not stop_game_completely:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -config.SNAKE_BLOCK; y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = config.SNAKE_BLOCK; y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -config.SNAKE_BLOCK; x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = config.SNAKE_BLOCK; x1_change = 0
                elif event.key == pygame.K_ESCAPE:
                    p_start = time.time()
                    duration, action = pause_menu(p_start)
                    total_pause_duration += duration
                    if action == 'restart': return 'restart'
                    if action == 'menu': return 'menu'

        if x1 >= config.WIDTH or x1 < 0 or y1 >= config.HEIGHT or y1 < 0:
            game_over = True
        
        x1 += x1_change
        y1 += y1_change
        
        config.dis.fill(config.BLACK)
        draw_grid()
        
        # Makanan Biasa
        pygame.draw.rect(config.dis, config.RED, [foodx, foody, config.SNAKE_BLOCK, config.SNAKE_BLOCK])

        current_time = time.time()
        elapsed_time = current_time - start_time - total_pause_duration

        # --- LOGIKA RACUN ---
        if not poison_active and (current_time - last_poison_spawn > poison_interval):
            poison_x, poison_y = get_random_position(snake_List)
            poison_active = True
            poison_start_time = current_time
            last_poison_spawn = current_time 

        if poison_active:
            time_left = poison_duration - (current_time - poison_start_time - total_pause_duration)
            if time_left <= 0:
                poison_active = False 
            else:
                pygame.draw.rect(config.dis, config.GREEN, [poison_x, poison_y, config.SNAKE_BLOCK, config.SNAKE_BLOCK])

        # --- LOGIKA BONUS ---
        if not bonus_food_active and elapsed_time >= next_bonus_spawn_time:
            bonus_x = round(random.randrange(0, config.WIDTH - bonus_size) / 10.0) * 10.0
            bonus_y = round(random.randrange(0, config.HEIGHT - bonus_size) / 10.0) * 10.0
            bonus_food_active = True
            bonus_start_time = current_time
            next_bonus_spawn_time += 30 

        if bonus_food_active:
            time_left = bonus_duration - (current_time - bonus_start_time - total_pause_duration)
            if time_left <= 0:
                bonus_food_active = False
            else:
                if time_left > 5 or int(current_time * 5) % 2 == 0:
                     pygame.draw.rect(config.dis, config.GOLD, [bonus_x, bonus_y, bonus_size, bonus_size])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        # --- LOGIKA PANJANG BADAN ---
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True

        our_snake(config.SNAKE_BLOCK, snake_List)
        utils.show_hud(current_score, elapsed_time, diff_str)
        
        record_text = config.info_font.render(f"Rekor: {top_score}", True, config.GRAY)
        config.dis.blit(record_text, [config.WIDTH/2 - 35, 30])

        if utils.button("||", config.WIDTH - 40, 40, 30, 30, config.DARK_GRAY, config.GRAY):
            p_start = time.time()
            duration, action = pause_menu(p_start)
            total_pause_duration += duration
            if action == 'restart': return 'restart'
            if action == 'menu': return 'menu'

        pygame.display.update()

        # Makan Apel Biasa
        if x1 == foodx and y1 == foody:
            foodx, foody = get_random_position(snake_List) 
            Length_of_snake += 1
            current_score += 1 

        # Makan Racun
        if poison_active and x1 == poison_x and y1 == poison_y:
            current_score -= 3
            Length_of_snake -= 3 
            
            # --- POTONG VISUAL BADAN ---
            for _ in range(3):
                if len(snake_List) > 1:
                    del snake_List[0]

            poison_active = False 
            
            if current_score < 0 or Length_of_snake < 1:
                game_over = True

        # Makan Apel Emas
        if bonus_food_active:
            if (x1 >= bonus_x and x1 < bonus_x + bonus_size) and (y1 >= bonus_y and y1 < bonus_y + bonus_size):
                Length_of_snake += 5 
                current_score += 5 
                bonus_food_active = False 

        if game_over:
            mins = int(elapsed_time // 60)
            secs = int(elapsed_time % 60)
            time_str = f"{mins:02d}:{secs:02d}"
            final_score_to_save = max(0, current_score)
            action = keluar.game_over_menu(final_score_to_save, diff_str, time_str)
            return action

        config.clock.tick(config.current_speed)

def main_menu():
    while True:
        config.dis.fill(config.BLACK)
        utils.draw_text_centered("Game Ular Sederhana", config.score_font, config.GREEN, config.dis, config.WIDTH/2, 80)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); quit()

        if utils.button("MAIN", 240, 150, 120, 50, config.GREEN, (100, 255, 100)):
            game_action = 'restart'
            while game_action == 'restart':
                game_action = gameLoop() 

        if utils.button("HIGH SCORE", 240, 210, 120, 50, config.YELLOW, config.WHITE):
            high_score.high_score_menu()

        if utils.button("SETTING", 240, 270, 120, 50, config.GRAY, config.WHITE):
            setting.settings_menu()
            
        if utils.button("KELUAR", 240, 330, 120, 50, config.RED, (255, 100, 100)):
            pygame.quit(); quit()

        pygame.display.update()
        config.clock.tick(15)

if __name__ == "__main__":
    try:
        high_score.load_data() 
        main_menu()
    except Exception as e:
        print(f"Terjadi error: {e}")
        pygame.quit()