import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, BooleanProperty, StringProperty
from kivy.graphics import Color, RoundedRectangle, Line, Ellipse, Rectangle
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivy.metrics import dp, sp

# --- DEFINIÇÃO DOS NÍVEIS ---
# (Matrizes idênticas à sua versão original)
LEVELS = {
    "Nível 1 (Fácil)": [
        ('hero', [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('h', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('h', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]]),
        ('h', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0]]),
        ('h', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0]]),
        ('h', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1]]),
    ],
    "Nível 2 (Fácil)": [
        ('hero', [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('h', [[0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('h', [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('h', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('h', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]),
        ('h', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]),
    ],
    "Nível 3 (Médio)": [
        ('hero', [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('h', [[0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('h', [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('h', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('v', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]),
        ('v', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]),
    ],
    "Nível 4 (Difícil)": [
        ('hero', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]),
        ('s', [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('h', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0]]),
        ('h', [[0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('h', [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ('v', [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]),
        ('v', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]),
        ('s', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]),
        ('h', [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0]]),
    ]
}

# Interface em KV Language (Muito mais rápido e leve que desenhar pixel a pixel)
KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex

<MenuButton@Button>:
    font_size: sp(18)
    bold: True
    background_normal: ''
    background_color: (1,1,1,1) if not self.disabled else (0.8, 0.8, 0.8, 1)
    color: (0.2, 0.3, 0.35, 1) if not self.disabled else (0.5, 0.5, 0.5, 1)
    canvas.before:
        Color:
            rgba: 0.74, 0.76, 0.78, 1
        Line:
            width: 1.5
            rounded_rectangle: (self.x, self.y, self.width, self.height, 10)

ScreenManager:
    MenuScreen:
    GameScreen:

<MenuScreen@Screen>:
    name: 'menu'
    canvas.before:
        Color:
            rgb: 0.94, 0.95, 0.96
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Label:
            text: "ESCAPE HERO"
            font_size: sp(45)
            bold: True
            color: 0.16, 0.5, 0.72, 1
            size_hint_y: 0.2
        ScrollView:
            GridLayout:
                id: level_grid
                cols: 1
                spacing: dp(15)
                size_hint_y: None
                height: self.minimum_height

<GameScreen@Screen>:
    name: 'game'
    canvas.before:
        Color:
            rgb: 0.94, 0.95, 0.96
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(15)
        BoxLayout:
            size_hint_y: 0.1
            spacing: dp(10)
            MenuButton:
                text: 'MENU'
                size_hint_x: 0.3
                on_release: app.root.current = 'menu'
            Label:
                id: title_lbl
                color: 0.2, 0.3, 0.4, 1
                bold: True
                font_size: sp(18)
            MenuButton:
                text: 'RESET'
                size_hint_x: 0.3
                on_release: board.reset_level()
        Label:
            id: info_lbl
            size_hint_y: 0.1
            color: 0.2, 0.3, 0.4, 1
            font_size: sp(18)
            bold: True
            text: "Moves: 0   |   Tempo: 00:00"
        AnchorLayout:
            size_hint_y: 0.8
            BoardWidget:
                id: board
                size_hint: None, None
'''


class Piece(Widget):
    def __init__(self, p_type, matrix, **kwargs):
        super().__init__(**kwargs)
        self.p_type = p_type
        # Cores convertidas para padrão Kivy (0-1)
        self.colors = {
            'hero': (135 / 255, 206 / 255, 250 / 255, 1),
            'v': (189 / 255, 195 / 255, 199 / 255, 1),
            'h': (230 / 255, 126 / 255, 34 / 255, 1),
            's': (255 / 255, 255 / 255, 0, 1)
        }

        # Converte a matriz do pygame para coordenadas (Kivy 0,0 é embaixo na esquerda)
        self.w, self.h, py_x, py_y = self.extract_geometry(matrix)
        self.grid_x = py_x
        self.grid_y = 5 - py_y - self.h  # Inverte o Y para o padrão Kivy

        self.dragging = False
        self.drag_axis = None

    def extract_geometry(self, matrix):
        min_x, min_y = 4, 5
        max_x, max_y = -1, -1
        found = False
        for r in range(5):
            for c in range(4):
                if matrix[r][c] == 1:
                    found = True
                    if c < min_x: min_x = c
                    if r < min_y: min_y = r
                    if c > max_x: max_x = c
                    if r > max_y: max_y = r
        if not found: return 1, 1, 0, 0
        w = (max_x - min_x) + 1
        h = (max_y - min_y) + 1
        return w, h, min_x, min_y

    def calculate_bounds(self, all_pieces):
        self.min_drag_x = 0
        self.max_drag_x = 4 - self.w
        self.min_drag_y = 0
        self.max_drag_y = 5 - self.h

        for p in all_pieces:
            if p is self: continue
            if not (p.grid_y >= self.grid_y + self.h or p.grid_y + p.h <= self.grid_y):
                if p.grid_x + p.w <= self.grid_x:
                    self.min_drag_x = max(self.min_drag_x, p.grid_x + p.w)
                elif p.grid_x >= self.grid_x + self.w:
                    self.max_drag_x = min(self.max_drag_x, p.grid_x - self.w)

            if not (p.grid_x >= self.grid_x + self.w or p.grid_x + p.w <= self.grid_x):
                if p.grid_y + p.h <= self.grid_y:
                    self.min_drag_y = max(self.min_drag_y, p.grid_y + p.h)
                elif p.grid_y >= self.grid_y + self.h:
                    self.max_drag_y = min(self.max_drag_y, p.grid_y - self.h)

    def update_rect(self):
        cs = self.parent.cell_size
        self.size = (self.w * cs, self.h * cs)
        self.pos = (self.parent.x + self.grid_x * cs, self.parent.y + self.grid_y * cs)

        self.canvas.clear()
        with self.canvas:
            if self.dragging:
                Color(0, 0, 0, 0.2)  # Sombra
                RoundedRectangle(pos=(self.x + 5, self.y - 5), size=self.size, radius=[8])

            Color(*self.colors[self.p_type])
            RoundedRectangle(pos=self.pos, size=self.size, radius=[8])

            Color(1, 1, 1, 1)  # Borda Branca
            Line(rounded_rectangle=(self.x, self.y, self.width, self.height, 8), width=1.5)

            if self.p_type == 'hero':
                Color(1, 1, 1, 1)
                Ellipse(pos=(self.center_x - dp(10), self.center_y - dp(10)), size=(dp(20), dp(20)))

    def on_touch_down(self, touch):
        app = App.get_running_app()
        if not app.won and self.collide_point(*touch.pos):
            touch.grab(self)
            self.dragging = True
            self.drag_axis = None
            self.touch_start_pos = touch.pos
            self.start_grid_x = self.grid_x
            self.start_grid_y = self.grid_y
            self.calculate_bounds(self.parent.pieces)

            # Traz a peça para frente visualmente
            self.parent.remove_widget(self)
            self.parent.add_widget(self)
            self.update_rect()
            return True
        return False

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            cs = self.parent.cell_size
            dx = (touch.x - self.touch_start_pos[0]) / cs
            dy = (touch.y - self.touch_start_pos[1]) / cs

            if self.drag_axis is None:
                if abs(dx * cs) > 10:
                    self.drag_axis = 'x'
                elif abs(dy * cs) > 10:
                    self.drag_axis = 'y'

            if self.drag_axis == 'x':
                self.grid_x = max(self.min_drag_x, min(self.start_grid_x + dx, self.max_drag_x))
            elif self.drag_axis == 'y':
                self.grid_y = max(self.min_drag_y, min(self.start_grid_y + dy, self.max_drag_y))

            self.update_rect()
            return True
        return False

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self.dragging = False

            new_x = round(self.grid_x)
            new_y = round(self.grid_y)

            if new_x != self.start_grid_x or new_y != self.start_grid_y:
                App.get_running_app().moves += 1

            self.grid_x = new_x
            self.grid_y = new_y
            self.update_rect()
            self.parent.check_win()
            return True
        return False


class BoardWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pieces = []
        self.cell_size = 100

    def on_size(self, *args):
        if self.parent:
            # Mantém a proporção exata para telas de celular
            self.cell_size = min(self.parent.width / 4.2, self.parent.height / 5.2)
            self.size = (self.cell_size * 4, self.cell_size * 5)
            self.draw_board()
            for p in self.pieces:
                p.update_rect()

    def draw_board(self):
        self.canvas.before.clear()
        with self.canvas.before:
            # Fundo escuro do tabuleiro
            Color(47 / 255, 54 / 255, 64 / 255, 1)
            RoundedRectangle(pos=(self.x - dp(10), self.y - dp(10)), size=(self.width + dp(20), self.height + dp(20)),
                             radius=[15])
            # Fundo claro
            Color(1, 1, 1, 1)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
            # Porta de Saída (Verde) na parte inferior
            Color(46 / 255, 204 / 255, 113 / 255, 1)
            Rectangle(pos=(self.x + self.cell_size, self.y - dp(10)), size=(self.cell_size * 2, dp(10)))

    def load_level(self, level_name):
        self.clear_widgets()
        self.pieces = []
        for p_type, matrix in LEVELS.get(level_name, []):
            p = Piece(p_type, matrix)
            self.add_widget(p)
            self.pieces.append(p)
        self.on_size()

    def reset_level(self):
        app = App.get_running_app()
        app.start_level(app.current_level)

    def check_win(self):
        for p in self.pieces:
            if p.p_type == 'hero' and p.grid_x == 1 and p.grid_y == 0:
                App.get_running_app().trigger_win()


class EscapeHeroApp(App):
    moves = NumericProperty(0)
    time_seconds = NumericProperty(0)
    won = BooleanProperty(False)

    def build(self):
        # Kivy gerencia o armazenamento de forma segura nativamente
        self.store = JsonStore(os.path.join(self.user_data_dir, 'progress.json'))
        self.max_unlocked = self.store.get('progress')['level'] if self.store.exists('progress') else 0
        self.level_names = list(LEVELS.keys())
        self.current_level = ""
        self.overlay = None

        self.sm = Builder.load_string(KV)
        self.populate_menu()
        Clock.schedule_interval(self.update_timer, 1)
        return self.sm

    def populate_menu(self):
        grid = self.sm.get_screen('menu').ids.level_grid
        grid.clear_widgets()
        for i, lvl_name in enumerate(self.level_names):
            # Cria botão local e previne recriação de escopo com o lambda
            btn = Factory.MenuButton(text=lvl_name, size_hint_y=None, height=dp(60))
            if i > self.max_unlocked:
                btn.disabled = True
            else:
                btn.bind(on_release=lambda instance, ln=lvl_name: self.start_level(ln))
            grid.add_widget(btn)

    def start_level(self, level_name):
        if self.overlay:
            self.sm.get_screen('game').remove_widget(self.overlay)
            self.overlay = None

        self.current_level = level_name
        self.moves = 0
        self.time_seconds = 0
        self.won = False

        game_screen = self.sm.get_screen('game')
        game_screen.ids.title_lbl.text = level_name
        game_screen.ids.info_lbl.text = "Moves: 0   |   Tempo: 00:00"
        game_screen.ids.board.load_level(level_name)

        self.sm.current = 'game'

    def update_timer(self, dt):
        if self.sm.current == 'game' and not self.won:
            self.time_seconds += 1
            mins = self.time_seconds // 60
            secs = self.time_seconds % 60
            self.sm.get_screen('game').ids.info_lbl.text = f"Moves: {self.moves}   |   Tempo: {mins:02}:{secs:02}"

    def trigger_win(self):
        self.won = True
        current_idx = self.level_names.index(self.current_level)

        # Desbloqueia próximo nível
        if current_idx == self.max_unlocked and current_idx < len(self.level_names) - 1:
            self.max_unlocked += 1
            self.store.put('progress', level=self.max_unlocked)
            self.populate_menu()

        # Cria a tela de vitória
        overlay = FloatLayout()
        with overlay.canvas.before:
            Color(1, 1, 1, 0.85)  # Fundo translúcido
            Rectangle(pos=self.sm.pos, size=self.sm.size)

        box = BoxLayout(orientation='vertical', size_hint=(0.8, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5},
                        spacing=dp(15))
        box.add_widget(Builder.load_string(
            f"Label:\n text: 'VITÓRIA!'\n font_size: sp(50)\n bold: True\n color: 0.16, 0.5, 0.72, 1"))

        mins, secs = self.time_seconds // 60, self.time_seconds % 60
        box.add_widget(Builder.load_string(
            f"Label:\n text: 'Movimentos: {self.moves} | Tempo: {mins:02}:{secs:02}'\n font_size: sp(18)\n color: 0,0,0,1"))

        if current_idx < len(self.level_names) - 1:
            next_lvl = self.level_names[current_idx + 1]
            btn_next = Factory.MenuButton(text="PRÓXIMO NÍVEL", size_hint_y=0.4,
                                          background_color=(46 / 255, 204 / 255, 113 / 255, 1), color=(1, 1, 1, 1))
            btn_next.bind(on_release=lambda x: self.start_level(next_lvl))
            box.add_widget(btn_next)

        btn_menu = Factory.MenuButton(text="VOLTAR AO MENU", size_hint_y=0.4)
        btn_menu.bind(on_release=lambda x: setattr(self.sm, 'current', 'menu'))
        box.add_widget(btn_menu)

        overlay.add_widget(box)
        self.sm.get_screen('game').add_widget(overlay)
        self.overlay = overlay


from kivy.factory import Factory

if __name__ == "__main__":
    EscapeHeroApp().run()
