import tkinter
import random
import time


# Документація для класу Ball (UA):
# Цей клас представляє м'яч у грі, подібній до Pong.
# Він керує рухом м'яча, зіткненнями з платформою та стінами,
# підрахунком очок та завершенням гри.

# Documentation for class Ball (EN):
# This class represents the ball in a Pong-like game.
# It manages the ball's movement, collisions with the paddle and walls,
# score counting, and game ending.


class Ball:
    """
    Клас Ball: М'яч у грі. (UA)

    Атрибути:
        - game_started: Логічне значення, чи розпочата гра (False за замовчуванням).
        - canvas: Об'єкт Canvas Tkinter для малювання.
        - paddle: Посилання на об'єкт Paddle (платформа).
        - score: Поточні очки (починається з 0).
        - score_id: ID тексту для відображення очок на canvas.
        - id: ID овалу (м'яча) на canvas.
        - x, y: Швидкості руху по осях (x - випадкова, y - -3).
        - canvas_height, canvas_width: Розміри canvas.
        - hit_bottom: Значення завершення гри (False за замовчуванням).

    Class Ball: The ball in the game. (EN)

        Attributes:
        - game_started: Boolean flag indicating if the game has started (default False).
        - canvas: Tkinter Canvas object for drawing.
        - paddle: Reference to the Paddle object.
        - score: Current score (starts at 0).
        - score_id: ID of the text displaying the score on canvas.
        - id: ID of the oval (ball) on canvas.
        - x, y: Movement speeds along axes (x random, y -3).
        - canvas_height, canvas_width: Dimensions of the canvas.
        - hit_bottom: Flag for game over (default False).
    """
    def __init__(self, canvas, paddle, fill_color, outline):
        self.game_started = False
        self.canvas = canvas
        self.paddle = paddle
        self.score = 0
        # Створення тексту для очок у верхньому лівому куті. (UA)
        # Creating score text in the top-left corner. (EN)
        self.score_id = canvas.create_text(10, 10,
                                           text=f'Score: {self.score}',
                                           font=('Courier', 16),
                                           fill='dark orange',
                                           anchor='nw'
                                           )
        # Створення овалу (м'яча) та переміщення до початкової позиції. (UA)
        # Creating the oval (ball) and moving to initial position. (EN)
        self.id = canvas.create_oval(10, 10, 25, 25,
                                     fill=fill_color,
                                     outline=outline
                                     )
        self.canvas.move(self.id, 245, 100)
        # Випадкова початкова швидкість по X. (UA)
        # Random initial speed along X. (EN)
        start = [-3, -2, -1, 1, 2, 3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def game_start(self, event):
        """
        Метод для старту гри. (UA)
            - Встановлює значення game_started на True при натисканні Enter.

        Method to start the game. (EN)
            - Sets the game_started flag to True on Enter press.
        """
        self.game_started = True

    def hit_paddle(self, pos):
        """
        Перевіряє зіткнення м'яча з платформою. (UA)

        Параметри:
            - pos: Координати м'яча.
                Повертає True, якщо зіткнення відбулося, і додає 10 очок.

        Checks for collision with the paddle. (EN)

        Parameters:
            - pos: Coordinates of the ball.
                Returns True if collision occurred, and adds 10 points.
        """
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]:
                self.score += 10
                return True
        return False

    def draw(self):
        """
        Малює та оновлює позицію м'яча. (UA)
            Обробляє відбиття від стін, зіткнення з платформою та завершення гри.

        Draws and updates the ball's position. (EN)
            Handles bounces off walls, paddle collision, and game end.
                """
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            # Відбиття від верхньої межі. (UA)
            # Bounce off top edge. (EN)
            self.y = 1.5

        if pos[3] >= self.canvas_height:
            # Відбиття від нижньої межі (але гра завершується). (UA)
            # Bounce off bottom (but game ends). (EN)
            self.y = -1.5

        if pos[3] >= self.canvas_height:
            # Створення тексту завершення гри. (UA)
            # Creating game over text. (EN)
            canvas.create_text(260, 250,
                               text=f'To be continued...\n'
                                    f'Score: {ball.score}',
                               fill='dark orange',
                               font=('Courier', 22, 'bold'),
                               )
            # Встановлення значення завершення гри. (UA)
            # Set game over flag. (EN)
            self.hit_bottom = True

        if self.hit_paddle(pos) == 1:
            # Відбиття від платформи. (UA)
            # Bounce off paddle. (EN)
            self.y = -2.5

        if pos[0] <= 0:
            # Відбиття від лівої межі. (UA)
            # Bounce off left edge. (EN)
            self.x = 1.5

        if pos[2] >= self.canvas_width:
            # Відбиття від правої межі. (UA)
            # Bounce off right edge. (EN)
            self.x = -1.5

# Документація для класу Paddle (UA):
# Цей клас представляє платформу (paddle) для відбиття м'яча.
# Керується стрілками ліворуч/праворуч.

# Documentation for class Paddle (EN):
# This class represents the paddle for bouncing the ball.
# Controlled by left/right arrow keys.

class Paddle:
    """
    Клас Paddle: Платформа для відбиття м'яча. (UA)

    Атрибути:
        - canvas: Об'єкт Canvas Tkinter.
        - id: ID прямокутника (платформи) на canvas.
        - x: Швидкість руху по X (0 за замовчуванням).
        - canvas_width: Ширина canvas.

    Class Paddle: Paddle for bouncing the ball. (EN)

    Attributes:
        - canvas: Tkinter Canvas object.
        - id: ID of the rectangle (paddle) on canvas.
        - x: Movement speed along X (default 0).
        - canvas_width: Width of the canvas.
    """
    def __init__(self, canvas, fill_color, outline):
        self.canvas = canvas
        # Створення прямокутника (платформи) та переміщення. (UA)
        # Creating rectangle (paddle) and moving. (EN)
        self.id = canvas.create_rectangle(0, 0, 100, 10,
                                          fill=fill_color,
                                          outline=outline
                                          )
        self.canvas.move(self.id, 200, 400)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        # Прив'язує клавіш для руху. (UA)
        # Binding keys for movement. (EN)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)


    def draw(self):
        """
        Малює та оновлює позицію платформи. (UA)
            Обмежує рух в межах екрану.

        Draws and updates the paddle's position. (EN)
             Limits movement within screen bounds.
        """
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        """
        Рух ліворуч: Встановлює x = -2. (UA)

        Move left: Sets x = -2. (EN)
        """
        self.x = -2

    def turn_right(self, evt):
        """
        Рух праворуч: Встановлює x = 2. (UA)

        Move right: Sets x = 2. (EN)
        """
        self.x = 2

# Документація для функції center_window (UA):
# Центрує вікно на екрані.

# Documentation for function center_window (EN):
# Centers the window on the screen.

def center_window(window, width, height):
    """
    Центрує вікно Tkinter на екрані. (UA)

    Параметри:
        - window: Об'єкт Tk.
        - width, height: Розміри вікна.

    Centers the Tkinter window on the screen. (EN)

    Parameters:
        - window: Tk object.
        - width, height: Window dimensions.
    """
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

# Головна частина програми: Створення вікна, полотна, об'єктів та циклу гри. (UA)
# Main program part: Creating window, canvas, objects, and game loop. (EN)

tk = tkinter.Tk()
# Центрування вікна 500x500. (UA)
# Centering 500x500 window. (EN)
center_window(tk, 500, 500)
tk.title(f'Game')

# Заборона зміни розміру. (UA)
# Disable resizing. (EN)
tk.resizable(False,False)

# Вікно поверх усіх. (UA)
# Window on top. (EN)
tk.wm_attributes('-topmost', True)
canvas = tkinter.Canvas(tk,
                        width=500,
                        height=500,
                        bd=0,
                        highlightthickness=3,
                        background='dark slate grey'
                        )
canvas.pack()
tk.update()

# Створення платформи. (UA)
# Creating paddle. (EN)
paddle = Paddle(canvas, 'dark orange', 'black')
# Створення м'яча. (UA)
# Creating ball. (EN)
ball = Ball(canvas, paddle, 'dark orange', 'black')

intro_text = canvas.create_text(250, 250,
                                text='Press "Enter" to start.',
                                fill='dark orange',
                                font=('Courier', 16, 'bold')
                                )

# Прив'язує Enter для старту. (UA)
# Binding Enter to start. (EN)
canvas.bind_all('<Return>', ball.game_start)



# Головний цикл гри. (UA)
# Main game loop. (EN)
while True:
    if ball.game_started and not ball.hit_bottom:
        # Видалення вступного тексту. (UA)
        # Delete intro text. (EN)
        canvas.delete(intro_text)

        # Оновлення м'яча. (UA)
        # Update ball. (EN)
        ball.draw()

        # Оновлення платформи. (UA)
        # Update paddle. (EN)
        paddle.draw()

    # Оновлення тексту очок. (UA)
    # Update score text. (EN)
    canvas.itemconfig(ball.score_id, text=f'Score: {ball.score}')
    tk.update_idletasks()
    tk.update()
    # Затримка для контролю швидкості (зменшення прискорить гру). (UA)
    # Delay for speed control (smaller value speeds up the game). (EN)
    time.sleep(0.003)




