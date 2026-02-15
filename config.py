import pygame

# Inisialisasi Pygame
pygame.init()

# --- Warna (RGB) ---
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
GRAY = (169, 169, 169)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
GOLD = (255, 215, 0)

# Warna 
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)

# --- Ukuran Layar ---
WIDTH = 600
HEIGHT = 400

dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game Ular Sederhana')

clock = pygame.time.Clock()

# --- Global Settings ---
SNAKE_BLOCK = 10
current_speed = 15  # Default speed
snake_color = BLUE  # Default skin (Biru)

# --- Font ---
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
button_font = pygame.font.SysFont("comicsansms", 20)
info_font = pygame.font.SysFont("comicsansms", 15)
input_font = pygame.font.SysFont("comicsansms", 30)