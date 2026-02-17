import pygame
import sys
import os
from pathlib import Path

# --- CONFIGURAÇÃO DE CAMINHOS ANDROID ---
def get_data_dir():
    """Retorna o diretório correto para salvar dados em Android ou Desktop"""
    if os.path.exists('/data/data'):  # Detecta se está em Android
        app_storage = Path.home() / 'Escape_Hero_Data'
        app_storage.mkdir(exist_ok=True)
        return str(app_storage)
    else:
        # Desktop: salva no mesmo diretório do app
        return os.getcwd()

DATA_DIR = get_data_dir()
PROGRESS_FILE = os.path.join(DATA_DIR, "progress.txt")

# --- Constantes e Configurações ---
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 850
GRID_OFFSET_X = 150
GRID_OFFSET_Y = 150
CELL_SIZE = 100
GRID_COLS = 4
GRID_ROWS = 5

# --- Cores ---
COLOR_BG = (240, 242, 245)
COLOR_BOARD_BG = (255, 255, 255)
COLOR_BOARD_BORDER = (47, 54, 64)

# Paleta do Jogo
COLOR_HERO = (135, 206, 250)    # Azul Claro
COLOR_BLOCK_H = (230, 126, 34)  # Laranja
COLOR_BLOCK_V = (189, 195, 199) # Cinza
COLOR_BLOCK_S = (255, 255, 0)   # Amarelo

# Cores da Interface (UI)
COLOR_TEXT = (44, 62, 80)
COLOR_TITLE = (41, 128, 185)

# Cores dos Botões
COLOR_BTN_UNLOCKED = (255, 255, 255)
COLOR_BTN_HOVER = (236, 240, 241)
COLOR_BTN_LOCKED = (200, 200, 200) 
COLOR_BTN_BORDER = (189, 195, 199)
COLOR_BTN_TEXT = (52, 73, 94)
COLOR_BTN_TEXT_LOCKED = (150, 150, 150)
COLOR_BTN_NEXT = (46, 204, 113) # Verde

# Tipos de Peças
TYPE_HERO = 'hero'
TYPE_V = 'v'
TYPE_H = 'h'
TYPE_S = 's'

# --- DEFINIÇÃO DOS NÍVEIS ---
LEVELS = {
    # --- NÍVEIS FÁCEIS ---
    "Nível 1 (Fácil)": [
        (TYPE_HERO, [[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S, [[0,0,0,0], [0,0,1,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_S, [[0,0,0,0], [0,0,0,1], [0,0,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_S, [[0,0,0,0], [0,0,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_S, [[0,0,0,0], [0,0,0,0], [0,1,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,0,0], [0,0,1,1], [0,0,0,0], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [1,1,0,0], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,1,1], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [1,1,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,1,1]]),
    ],
    "Nível 2 (Fácil)": [
        (TYPE_HERO, [[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,1,1], [0,0,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,0,0], [1,1,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,0,0], [0,0,1,1], [0,0,0,0], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,1,1,0], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,1,1,0]]),
        (TYPE_S, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [1,0,0,0], [0,0,0,0]]),
        (TYPE_S, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,1], [0,0,0,0]]),
        (TYPE_S, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [1,0,0,0]]),
        (TYPE_S, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,1]]),
    ],
    "Nível 3 (Fácil)": [
        (TYPE_HERO, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,1],[0,0,1,1]]),
        (TYPE_S, [[1,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_S, [[0,1,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_S, [[0,0,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_S, [[0,0,0,0], [0,1,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_H, [[0,0,1,1], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,1,1], [0,0,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,0,0], [1,1,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,0,0], [0,0,1,1], [0,0,0,0], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [1,1,0,0], [0,0,0,0]]),
    ],
    "Nível 4 (Fácil)": [
        (TYPE_HERO, [[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H, [[0,0,1,1], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,1,1], [0,0,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,1,1], [0,0,0,0]]),
        (TYPE_H, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,1,1,0]]),
        (TYPE_V, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [1,0,0,0], [1,0,0,0]]),
        (TYPE_S, [[0,0,0,0], [0,0,0,0], [0,1,0,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_S, [[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,0], [0,0,0,0]]),
        (TYPE_S, [[0,0,0,0], [0,0,0,0], [0,0,0,1], [0,0,0,0], [0,0,0,0]]),
        (TYPE_S, [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,1]]),
    ],

    # --- NÍVEIS MÉDIOS ---
    "Nível 5 (Médio)": [
        (TYPE_HERO, [[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,1,1],[0,0,0,0],[0,0,0,0]]),
        (TYPE_V,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0],[1,0,0,0]]),
        (TYPE_V,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,0,0],[0,1,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]),
    ],
    "Nível 6 (Médio)": [
        (TYPE_HERO, [[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_V,    [[0,0,0,0],[0,0,0,0],[1,0,0,0],[1,0,0,0],[0,0,0,0]]),
        (TYPE_V,    [[0,0,0,0],[0,0,0,0],[0,1,0,0],[0,1,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,1,1],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,1],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,0,0]]),
    ],
    "Nível 7 (Médio)": [
        (TYPE_HERO, [[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_V,    [[0,0,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_V,    [[0,0,0,0],[0,0,0,1],[0,0,0,1],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]),
        (TYPE_V,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0],[1,0,0,0]]),
        (TYPE_V,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,1]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,1,0]]),
    ],
    "Nível 8 (Médio)": [
        (TYPE_HERO, [[0,0,0,0],[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]),
        (TYPE_S,    [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,1,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_V,    [[0,0,0,0],[0,0,0,0],[1,0,0,0],[1,0,0,0],[0,0,0,0]]),
        (TYPE_V,    [[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,1],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,1]]),
    ],

    # --- NÍVEIS DIFÍCEIS ---
    "Nível 9 (Difícil)": [
        (TYPE_HERO, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,1],[0,0,1,1]]),
        (TYPE_V,    [[1,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,1,1],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,0,0]]),
    ],
    "Nível 10 (Difícil)": [
        (TYPE_HERO, [[0,0,0,0],[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]),
        (TYPE_S,    [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,1,0]]),
        (TYPE_H,    [[0,0,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_V,    [[0,0,0,0],[0,0,0,0],[1,0,0,0],[1,0,0,0],[0,0,0,0]]),
        (TYPE_V,    [[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,1],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,1,0]]),
    ],
    "Nível 11 (Difícil)": [
        (TYPE_HERO, [[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_V,    [[1,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,1,1],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,1],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]),
    ],
    "Nível 12 (Difícil)": [
        (TYPE_HERO, [[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_V,    [[1,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_V,    [[0,0,0,1],[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_H,    [[0,0,0,0],[0,0,0,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]]),
        (TYPE_V,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0],[1,0,0,0]]),
        (TYPE_V,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,1]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,0,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]),
        (TYPE_S,    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,0]]),
    ]
}

class Piece:
    def __init__(self, matrix, p_type):
        self.type = p_type
        self.grid_x, self.grid_y, self.w, self.h = self.extract_geometry(matrix)
        self.rect = pygame.Rect(0, 0, self.w * CELL_SIZE, self.h * CELL_SIZE)
        self.update_rect_position()
        
        self.dragging = False
        self.drag_offset_x = 0
        self.drag_offset_y = 0
        self.min_drag_x = 0; self.max_drag_x = 0
        self.min_drag_y = 0; self.max_drag_y = 0
        self.drag_axis = None

    def extract_geometry(self, matrix):
        min_x, min_y = GRID_COLS, GRID_ROWS
        max_x, max_y = -1, -1
        found = False
        for r in range(GRID_ROWS):
            for c in range(GRID_COLS):
                if matrix[r][c] == 1:
                    found = True
                    if c < min_x: min_x = c
                    if r < min_y: min_y = r
                    if c > max_x: max_x = c
                    if r > max_y: max_y = r
        if not found: return 0, 0, 1, 1
        return min_x, min_y, (max_x - min_x) + 1, (max_y - min_y) + 1

    def update_rect_position(self):
        self.rect.x = GRID_OFFSET_X + self.grid_x * CELL_SIZE
        self.rect.y = GRID_OFFSET_Y + self.grid_y * CELL_SIZE

    def calculate_bounds(self, all_pieces):
        self.min_drag_x = GRID_OFFSET_X
        self.max_drag_x = GRID_OFFSET_X + (GRID_COLS - self.w) * CELL_SIZE
        self.min_drag_y = GRID_OFFSET_Y
        self.max_drag_y = GRID_OFFSET_Y + (GRID_ROWS - self.h) * CELL_SIZE

        for p in all_pieces:
            if p is self: continue
            if not (p.grid_y >= self.grid_y + self.h or p.grid_y + p.h <= self.grid_y):
                if p.grid_x + p.w <= self.grid_x:
                    limit = GRID_OFFSET_X + (p.grid_x + p.w) * CELL_SIZE
                    if limit > self.min_drag_x: self.min_drag_x = limit
                elif p.grid_x >= self.grid_x + self.w:
                    limit = GRID_OFFSET_X + (p.grid_x - self.w) * CELL_SIZE
                    if limit < self.max_drag_x: self.max_drag_x = limit
            if not (p.grid_x >= self.grid_x + self.w or p.grid_x + p.w <= self.grid_x):
                if p.grid_y + p.h <= self.grid_y:
                    limit = GRID_OFFSET_Y + (p.grid_y + p.h) * CELL_SIZE
                    if limit > self.min_drag_y: self.min_drag_y = limit
                elif p.grid_y >= self.grid_y + self.h:
                    limit = GRID_OFFSET_Y + (p.grid_y - self.h) * CELL_SIZE
                    if limit < self.max_drag_y: self.max_drag_y = limit

    def draw(self, surface):
        colors = {TYPE_HERO: COLOR_HERO, TYPE_V: COLOR_BLOCK_V, TYPE_H: COLOR_BLOCK_H, TYPE_S: COLOR_BLOCK_S}
        color = colors.get(self.type, (100, 100, 100))
        
        if self.dragging:
            s = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)
            pygame.draw.rect(s, (0, 0, 0, 50), s.get_rect(), border_radius=8)
            surface.blit(s, (self.rect.x + 5, self.rect.y + 5))

        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 2, border_radius=8)
        if self.type == TYPE_HERO:
            pygame.draw.circle(surface, (255, 255, 255), self.rect.center, 15)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Escape Hero - Python Edition")
        self.clock = pygame.time.Clock()
        
        self.font_ui = pygame.font.SysFont("Segoe UI", 20, bold=True)
        self.font_title = pygame.font.SysFont("Segoe UI", 60, bold=True)
        self.font_btn = pygame.font.SysFont("Segoe UI", 18, bold=True)
        self.font_header = pygame.font.SysFont("Segoe UI", 24, bold=True)
        
        self.state = "MENU"
        self.current_level_name = "Nível 1 (Fácil)"
        self.pieces = []
        self.moves = 0
        self.won = False
        
        # Variáveis de Tempo
        self.start_ticks = 0
        self.final_time_str = "00:00"

        # --- Lógica de Progressão ---
        self.level_list = list(LEVELS.keys())
        self.max_unlocked_index = 0 
        self.load_progress() 

        # --- Configuração das 3 Colunas do Menu ---
        self.menu_buttons = []
        columns = {"Fácil": [], "Médio": [], "Difícil": []}
        
        for lvl_name in LEVELS.keys():
            if "Fácil" in lvl_name: columns["Fácil"].append(lvl_name)
            elif "Médio" in lvl_name: columns["Médio"].append(lvl_name)
            elif "Difícil" in lvl_name: columns["Difícil"].append(lvl_name)
        
        col_centers = [116, 350, 583]
        btn_width = 180; btn_height = 50
        start_y = 350; gap_y = 60
        col_keys = ["Fácil", "Médio", "Difícil"]
        
        for i, key in enumerate(col_keys):
            for j, lvl_name in enumerate(columns[key]):
                rect = pygame.Rect(0, 0, btn_width, btn_height)
                rect.centerx = col_centers[i]
                rect.y = start_y + j * gap_y
                self.menu_buttons.append({
                    "text": f"Nível {lvl_name.split()[1]}",
                    "rect": rect, "action": lvl_name, "category": key
                })

    def load_progress(self):
        """Carrega o progresso salvo de forma segura (Android-compatível)"""
        try:
            if os.path.exists(PROGRESS_FILE):
                with open(PROGRESS_FILE, "r") as f:
                    content = f.read().strip()
                    if content:
                        self.max_unlocked_index = int(content)
        except Exception as e:
            print(f"Erro ao carregar progresso: {e}")
            self.max_unlocked_index = 0

    def save_progress(self):
        """Salva o progresso de forma segura (Android-compatível)"""
        try:
            with open(PROGRESS_FILE, "w") as f:
                f.write(str(self.max_unlocked_index))
        except Exception as e:
            print(f"Erro ao salvar progresso: {e}")

    def load_level(self, level_name):
        self.current_level_name = level_name
        data = LEVELS.get(level_name, [])
        self.pieces = []
        for (p_type, matrix) in data:
            self.pieces.append(Piece(matrix, p_type))
        self.moves = 0
        self.won = False
        self.start_ticks = pygame.time.get_ticks() # Reinicia timer
        self.state = "PLAYING"

    def handle_input(self):
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if self.state == "MENU":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for btn in self.menu_buttons:
                        if btn["rect"].collidepoint(mx, my):
                            lvl_idx = self.level_list.index(btn["action"])
                            if lvl_idx <= self.max_unlocked_index:
                                self.load_level(btn["action"])
            
            elif self.state == "PLAYING":
                if self.won:
                    # Lógica de clique na tela de vitória
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Botão Menu na tela de vitória
                        menu_rect = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 80, 200, 50)
                        if menu_rect.collidepoint(mx, my):
                            self.state = "MENU"
                            return
                        
                        # Botão Próximo Nível (Se não for o último)
                        current_idx = self.level_list.index(self.current_level_name)
                        if current_idx < len(self.level_list) - 1:
                            next_rect = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 20, 200, 50)
                            if next_rect.collidepoint(mx, my):
                                next_lvl = self.level_list[current_idx + 1]
                                self.load_level(next_lvl)
                                return

                # Lógica normal de jogo (Arrastar peças)
                if event.type == pygame.MOUSEBUTTONDOWN and not self.won:
                    back_btn = pygame.Rect(20, 20, 100, 40)
                    if back_btn.collidepoint(mx, my):
                        self.state = "MENU"; return
                    
                    # Botão Reset
                    reset_btn = pygame.Rect(SCREEN_WIDTH - 120, 20, 100, 40)
                    if reset_btn.collidepoint(mx, my):
                        self.load_level(self.current_level_name)
                        return

                    for p in reversed(self.pieces):
                        if p.rect.collidepoint(mx, my):
                            p.dragging = True
                            p.drag_offset_x = p.rect.x - mx
                            p.drag_offset_y = p.rect.y - my
                            p.drag_axis = None
                            p.calculate_bounds(self.pieces)
                            break

                elif event.type == pygame.MOUSEBUTTONUP:
                    for p in self.pieces:
                        if p.dragging:
                            p.dragging = False
                            nx = round((p.rect.x - GRID_OFFSET_X) / CELL_SIZE)
                            ny = round((p.rect.y - GRID_OFFSET_Y) / CELL_SIZE)
                            if nx != p.grid_x or ny != p.grid_y:
                                self.moves += 1
                                p.grid_x, p.grid_y = int(nx), int(ny)
                            p.update_rect_position()
                            if p.type == TYPE_HERO and p.grid_x == 1 and p.grid_y == 3:
                                self.won = True
                                # Calcular e salvar tempo final
                                total_seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
                                mins = total_seconds // 60
                                secs = total_seconds % 60
                                self.final_time_str = f"{mins:02}:{secs:02}"
                                
                                current_idx = self.level_list.index(self.current_level_name)
                                if current_idx == self.max_unlocked_index:
                                    if self.max_unlocked_index < len(self.level_list) - 1:
                                        self.max_unlocked_index += 1
                                        self.save_progress()

        if self.state == "PLAYING":
            for p in self.pieces:
                if p.dragging:
                    tx, ty = mx + p.drag_offset_x, my + p.drag_offset_y
                    if p.drag_axis is None:
                        if abs(tx - p.rect.x) > 10: p.drag_axis = 'x'
                        elif abs(ty - p.rect.y) > 10: p.drag_axis = 'y'
                    if p.drag_axis == 'x':
                        p.rect.x = max(p.min_drag_x, min(tx, p.max_drag_x))
                        p.rect.y = GRID_OFFSET_Y + p.grid_y * CELL_SIZE
                    elif p.drag_axis == 'y':
                        p.rect.y = max(p.min_drag_y, min(ty, p.max_drag_y))
                        p.rect.x = GRID_OFFSET_X + p.grid_x * CELL_SIZE

    def draw_menu(self):
        title_shadow = self.font_title.render("ESCAPE HERO", True, (200, 200, 200))
        title = self.font_title.render("ESCAPE HERO", True, (41, 128, 185))
        self.screen.blit(title_shadow, (SCREEN_WIDTH//2 - title.get_width()//2 + 4, 84))
        self.screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 80))
        
        col_centers = [116, 350, 583]
        headers = ["FÁCIL", "MÉDIO", "DIFÍCIL"]
        colors = [(46, 204, 113), (241, 196, 15), (231, 76, 60)]
        for i, header in enumerate(headers):
            txt = self.font_header.render(header, True, colors[i])
            pygame.draw.line(self.screen, colors[i], (col_centers[i]-40, 310), (col_centers[i]+40, 310), 3)
            self.screen.blit(txt, (col_centers[i] - txt.get_width()//2, 280))

        mx, my = pygame.mouse.get_pos()
        for btn in self.menu_buttons:
            lvl_idx = self.level_list.index(btn["action"])
            is_unlocked = lvl_idx <= self.max_unlocked_index
            
            is_hover = btn["rect"].collidepoint(mx, my) and is_unlocked
            if is_unlocked:
                bg_color = COLOR_BTN_HOVER if is_hover else COLOR_BTN_UNLOCKED
                text_color = COLOR_BTN_TEXT
            else:
                bg_color = COLOR_BTN_LOCKED
                text_color = COLOR_BTN_TEXT_LOCKED

            shadow_rect = btn["rect"].copy()
            shadow_rect.y += 3
            pygame.draw.rect(self.screen, (200, 200, 200), shadow_rect, border_radius=10)
            pygame.draw.rect(self.screen, bg_color, btn["rect"], border_radius=10)
            pygame.draw.rect(self.screen, (189, 195, 199), btn["rect"], 2, border_radius=10)
            txt = self.font_btn.render(btn["text"], True, text_color)
            self.screen.blit(txt, (btn["rect"].centerx - txt.get_width()//2, btn["rect"].centery - txt.get_height()//2))
            
            if not is_unlocked:
                lock = self.font_btn.render("X", True, (100,100,100))
                self.screen.blit(lock, (btn["rect"].right - 20, btn["rect"].centery - lock.get_height()//2))

    def draw_game(self):
        # UI Topo
        back_rect = pygame.Rect(20, 20, 100, 40)
        pygame.draw.rect(self.screen, (255, 255, 255), back_rect, border_radius=8)
        pygame.draw.rect(self.screen, (189, 195, 199), back_rect, 2, border_radius=8)
        txt_back = self.font_ui.render("MENU", True, (52, 73, 94))
        self.screen.blit(txt_back, (back_rect.centerx - txt_back.get_width()//2, back_rect.centery - txt_back.get_height()//2))
        
        # Reset Button
        reset_rect = pygame.Rect(SCREEN_WIDTH - 120, 20, 100, 40)
        pygame.draw.rect(self.screen, (255, 255, 255), reset_rect, border_radius=8)
        pygame.draw.rect(self.screen, (189, 195, 199), reset_rect, 2, border_radius=8)
        txt_reset = self.font_ui.render("RESET", True, (52, 73, 94))
        self.screen.blit(txt_reset, (reset_rect.centerx - txt_reset.get_width()//2, reset_rect.centery - txt_reset.get_height()//2))

        # Stats (Moves e Tempo)
        if not self.won:
            secs = (pygame.time.get_ticks() - self.start_ticks) // 1000
            current_time = f"{secs//60:02}:{secs%60:02}"
        else:
            current_time = self.final_time_str

        # Título Nível
        title = self.font_ui.render(f"{self.current_level_name}", True, (44, 62, 80))
        self.screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 20))
        
        # Info Bar
        info_str = f"Moves: {self.moves}   |   Tempo: {current_time}"
        info_txt = self.font_ui.render(info_str, True, (44, 62, 80))
        self.screen.blit(info_txt, (SCREEN_WIDTH//2 - info_txt.get_width()//2, 60))

        # Tabuleiro
        board_rect = pygame.Rect(GRID_OFFSET_X - 10, GRID_OFFSET_Y - 10, GRID_COLS * CELL_SIZE + 20, GRID_ROWS * CELL_SIZE + 20)
        pygame.draw.rect(self.screen, (47, 54, 64), board_rect, border_radius=15)
        pygame.draw.rect(self.screen, (255, 255, 255), board_rect.inflate(-10, -10), border_radius=10)
        
        exit_r = pygame.Rect(GRID_OFFSET_X + CELL_SIZE, GRID_OFFSET_Y + GRID_ROWS * CELL_SIZE, CELL_SIZE * 2, 10)
        pygame.draw.rect(self.screen, (46, 204, 113), exit_r, border_bottom_left_radius=10, border_bottom_right_radius=10)

        top_piece = None
        for p in self.pieces:
            if p.dragging: top_piece = p
            else: p.draw(self.screen)
        if top_piece: top_piece.draw(self.screen)

        if self.won:
            over = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            over.fill((255, 255, 255, 230))
            self.screen.blit(over, (0, 0))
            
            # Título Vitória
            win_txt = self.font_title.render("VITÓRIA!", True, (41, 128, 185))
            self.screen.blit(win_txt, (SCREEN_WIDTH//2 - win_txt.get_width()//2, SCREEN_HEIGHT//2 - 120))
            
            # Estatísticas Finais
            stats_str = f"Movimentos: {self.moves}   |   Tempo: {self.final_time_str}"
            stats_render = self.font_ui.render(stats_str, True, (44, 62, 80))
            self.screen.blit(stats_render, (SCREEN_WIDTH//2 - stats_render.get_width()//2, SCREEN_HEIGHT//2 - 50))
            
            # Botão Próximo Nível (Se não for o último)
            current_idx = self.level_list.index(self.current_level_name)
            
            if current_idx < len(self.level_list) - 1:
                next_rect = pygame.Rect(SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 + 20, 240, 50)
                mx, my = pygame.mouse.get_pos()
                col = COLOR_BTN_NEXT
                if next_rect.collidepoint(mx, my):
                    col = (39, 174, 96) # Darker Green
                
                pygame.draw.rect(self.screen, col, next_rect, border_radius=10)
                pygame.draw.rect(self.screen, (30, 130, 76), next_rect, 2, border_radius=10)
                txt_next = self.font_btn.render("PRÓXIMO NÍVEL", True, (255, 255, 255))
                self.screen.blit(txt_next, (next_rect.centerx - txt_next.get_width()//2, next_rect.centery - txt_next.get_height()//2))

            # Botão Menu
            menu_rect = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 90, 200, 50)
            mx, my = pygame.mouse.get_pos()
            col_m = COLOR_BTN_UNLOCKED
            if menu_rect.collidepoint(mx, my): col_m = COLOR_BTN_HOVER
            
            pygame.draw.rect(self.screen, col_m, menu_rect, border_radius=10)
            pygame.draw.rect(self.screen, COLOR_BTN_BORDER, menu_rect, 2, border_radius=10)
            txt_menu = self.font_btn.render("VOLTAR AO MENU", True, COLOR_BTN_TEXT)
            self.screen.blit(txt_menu, (menu_rect.centerx - txt_menu.get_width()//2, menu_rect.centery - txt_menu.get_height()//2))

    def draw(self):
        self.screen.fill((240, 242, 245))
        if self.state == "MENU": self.draw_menu()
        elif self.state == "PLAYING": self.draw_game()
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_input()
            self.draw()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()
