import tkinter as tk
import random

# Constants
WIDTH, HEIGHT = 800, 400
BALL_SIZE = 20
PLAYER_WIDTH = 10    # Width of the stick
PLAYER_HEIGHT = 80   # Height of the stick
GOAL_WIDTH = 120      # Width of the goal
GOAL_DEPTH = 130       # Depth (height) of the goal
WHITE = "white"
GREEN = "green"
DARK_GREEN = "dark green"
BLACK = "black"
RED = "red"
BLUE = "blue"
FPS = 60
FONT_SIZE = 15
BALL_SPEED = 4
PLAYER_SPEED = 10
WINNING_SCORE = 5  # Target score to win the game
WINNER_FONT_SIZE = 50  # Font size for the winner message

class BallTapBattle:
    def __init__(self, root):
        self.root = root
        self.root.title("Ball Tap Battle")
        
        # Initialize variables
        self.ball_x = WIDTH // 2
        self.ball_y = HEIGHT // 2
        self.ball_dx = BALL_SPEED
        self.ball_dy = BALL_SPEED
        
        # Adjust player positions to be outside the goals
        self.player1_x = GOAL_WIDTH + 10  # Position player 1 just outside the left goal
        self.player1_y = HEIGHT // 2 - PLAYER_HEIGHT // 2
        self.player2_x = WIDTH - GOAL_WIDTH - PLAYER_WIDTH - 10  # Position player 2 just outside the right goal
        self.player2_y = HEIGHT // 2 - PLAYER_HEIGHT // 2
        
        self.goal1_x = 0
        self.goal1_y = HEIGHT // 2 - GOAL_DEPTH // 2
        self.goal2_x = WIDTH - GOAL_WIDTH
        self.goal2_y = HEIGHT // 2 - GOAL_DEPTH // 2
        self.score1 = 0
        self.score2 = 0
        
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=GREEN)
        self.canvas.pack()
        
        self.font = ("Arial", FONT_SIZE)
        
        self.menu_active = True
        self.game_active = False
        self.game_over = False

        self.draw_menu()
        
        # Bind keys to movement functions
        self.root.bind("<KeyPress-w>", self.start_move_player1_up)
        self.root.bind("<KeyPress-s>", self.start_move_player1_down)
        self.root.bind("<KeyPress-Up>", self.start_move_player2_up)
        self.root.bind("<KeyPress-Down>", self.start_move_player2_down)
        self.root.bind("<KeyRelease-w>", self.stop_move_player1)
        self.root.bind("<KeyRelease-s>", self.stop_move_player1)
        self.root.bind("<KeyRelease-Up>", self.stop_move_player2)
        self.root.bind("<KeyRelease-Down>", self.stop_move_player2)

        # Movement direction
        self.move_player1_up = False
        self.move_player1_down = False
        self.move_player2_up = False
        self.move_player2_down = False

    def draw_menu(self):
        self.canvas.delete("all")
        self.canvas.create_text(WIDTH // 2, HEIGHT // 4, text="Ball Tap Battle", font=self.font, fill=BLACK)
        
        # Player 1 Name
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2 - 50, text="Player 1 Name:", font=self.font, fill=BLACK)
        self.player1_name_entry = tk.Entry(self.root, font=self.font)
        self.player1_name_entry.place(x=WIDTH // 2 - 100, y=HEIGHT // 2 - 20, width=200)
        
        # Player 2 Name
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2 + 50, text="Player 2 Name:", font=self.font, fill=BLACK)
        self.player2_name_entry = tk.Entry(self.root, font=self.font)
        self.player2_name_entry.place(x=WIDTH // 2 - 100, y=HEIGHT // 2 + 80, width=200)
        
        # Start Button
        self.start_button = tk.Button(self.root, text="Start Game", font=self.font, command=self.start_game)
        self.start_button.place(x=WIDTH // 2 - 100, y=HEIGHT // 2 + 150, width=200, height=50)
        
    def draw_game(self):
        self.canvas.delete("all")
        
        # Draw field lines
        self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, outline=WHITE, width=5)  # Outer boundary
        self.canvas.create_line(WIDTH // 2, 0, WIDTH // 2, HEIGHT, fill=WHITE)  # Center line
        self.canvas.create_oval(WIDTH // 2 - 50, HEIGHT // 2 - 50, WIDTH // 2 + 50, HEIGHT // 2 + 50, outline=WHITE, width=2)  # Center circle
        self.canvas.create_rectangle(self.goal1_x, self.goal1_y, self.goal1_x + GOAL_WIDTH, self.goal1_y + GOAL_DEPTH, outline=WHITE, width=2)  # Left goal
        self.canvas.create_rectangle(self.goal2_x, self.goal2_y, self.goal2_x + GOAL_WIDTH, self.goal2_y + GOAL_DEPTH, outline=WHITE, width=2)  # Right goal
        
        # Draw players as sticks
        self.canvas.create_rectangle(self.player1_x, self.player1_y, self.player1_x + PLAYER_WIDTH, self.player1_y + PLAYER_HEIGHT, fill=RED)
        self.canvas.create_rectangle(self.player2_x, self.player2_y, self.player2_x + PLAYER_WIDTH, self.player2_y + PLAYER_HEIGHT, fill=BLUE)
        
        self.canvas.create_oval(self.ball_x, self.ball_y, self.ball_x + BALL_SIZE, self.ball_y + BALL_SIZE, fill=BLACK)
        
        score_text = f"{self.player1_name}: {self.score1}    {self.player2_name}: {self.score2}"
        self.canvas.create_text(WIDTH // 2, 10, text=score_text, font=self.font, fill=WHITE)
        
        # Display winner message if game is over
        if self.game_over:
            winner = self.player1_name if self.score1 >= WINNING_SCORE else self.player2_name
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text=f"{winner} Wins!", font=("Arial", WINNER_FONT_SIZE), fill=WHITE)

    def start_move_player1_up(self, event):
        self.move_player1_up = True
    
    def start_move_player1_down(self, event):
        self.move_player1_down = True
    
    def start_move_player2_up(self, event):
        self.move_player2_up = True
    
    def start_move_player2_down(self, event):
        self.move_player2_down = True

    def stop_move_player1(self, event):
        self.move_player1_up = False
        self.move_player1_down = False
    
    def stop_move_player2(self, event):
        self.move_player2_up = False
        self.move_player2_down = False

    def start_game(self):
        self.player1_name = self.player1_name_entry.get() or "Player 1"
        self.player2_name = self.player2_name_entry.get() or "Player 2"
        self.menu_active = False
        self.game_active = True
        self.game_over = False
        self.player1_name_entry.destroy()
        self.player2_name_entry.destroy()
        self.start_button.destroy()
        self.update()

    def update(self):
        if self.menu_active:
            self.draw_menu()
        elif self.game_active:
            # Move players
            if self.move_player1_up:
                self.player1_y = max(0, self.player1_y - PLAYER_SPEED)
            if self.move_player1_down:
                self.player1_y = min(HEIGHT - PLAYER_HEIGHT, self.player1_y + PLAYER_SPEED)
            if self.move_player2_up:
                self.player2_y = max(0, self.player2_y - PLAYER_SPEED)
            if self.move_player2_down:
                self.player2_y = min(HEIGHT - PLAYER_HEIGHT, self.player2_y + PLAYER_SPEED)
            
            # Move ball
            self.ball_x += self.ball_dx
            self.ball_y += self.ball_dy
            self.handle_collision()
            self.draw_game()
        
        self.root.after(1000 // FPS, self.update)

    def handle_collision(self):
        if self.ball_x <= self.goal1_x + GOAL_WIDTH and self.goal1_y <= self.ball_y + BALL_SIZE and self.ball_y <= self.goal1_y + GOAL_DEPTH:
            self.score2 += 1
            self.reset_ball()
            if self.score2 >= WINNING_SCORE:
                self.game_active = False
                self.game_over = True
        if self.ball_x + BALL_SIZE >= self.goal2_x and self.goal2_y <= self.ball_y + BALL_SIZE and self.ball_y <= self.goal2_y + GOAL_DEPTH:
            self.score1 += 1
            self.reset_ball()
            if self.score1 >= WINNING_SCORE:
                self.game_active = False
                self.game_over = True

        if self.ball_x < 0 or self.ball_x + BALL_SIZE > WIDTH:
            self.ball_dx = -self.ball_dx
        if self.ball_y < 0 or self.ball_y + BALL_SIZE > HEIGHT:
            self.ball_dy = -self.ball_dy

        if self.ball_x <= self.player1_x + PLAYER_WIDTH and self.player1_y <= self.ball_y + BALL_SIZE and self.ball_y <= self.player1_y + PLAYER_HEIGHT:
            self.ball_dx = -self.ball_dx
        if self.ball_x + BALL_SIZE >= self.player2_x and self.player2_y <= self.ball_y + BALL_SIZE and self.ball_y <= self.player2_y + PLAYER_HEIGHT:
            self.ball_dx = -self.ball_dx

    def reset_ball(self):
        self.ball_x = WIDTH // 2
        self.ball_y = HEIGHT // 2
        self.ball_dx = random.choice([-BALL_SPEED, BALL_SPEED])
        self.ball_dy = random.choice([-BALL_SPEED, BALL_SPEED])

if __name__ == "__main__":
    root = tk.Tk()
    game = BallTapBattle(root)
    root.mainloop()
