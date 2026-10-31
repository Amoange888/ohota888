import tkinter as tk

COLS = 30
ROWS = 15
CELL_SIZE = 25
import random
RABBIT_COUNT = 65
WOLF_COUNT = 40
rabbits = []
wolves = []

for i in range(RABBIT_COUNT):
    rabbit = {
        "x": random.randint(0, COLS - 1),
        "y": random.randint(0, ROWS - 1)
    }
    rabbits.append(rabbit)

for i in range(WOLF_COUNT):
    wolf = {
        "x": random.randint(0,COLS - 1),
        "y": random.randint(0,ROWS - 1)

    }
    wolves.append(wolf)
root = tk.Tk()
root.title("Симуляция экосистемы")

canvas = tk.Canvas(
    root,
    width=COLS * CELL_SIZE,
    height=ROWS * CELL_SIZE
)
canvas.pack(padx = 10, pady = 10)

for row in range(ROWS):
    for col in range(COLS):
        x1 = col * CELL_SIZE
        y1 = row * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        canvas.create_rectangle(
            x1, y1, x2, y2,
            outline = 'BLACK'

        )
def move_animals(animals):
    for animal in animals:
        animal["x"] += random.randint(-1, 1)
        animal["y"] += random.randint(-1, 1)
        animal["x"] = max(0, min(COLS -1, animal["x"]))
        animal["y"] = max(0, min(ROWS - 1, animal["y"]))

def hunt():
    for wolf in wolves:
        for rabbit in rabbits[:]:
            if wolf["x"] == rabbit["x"] and wolf["y"] == rabbit["y"]:
                rabbits.remove(rabbit)
                break

def next_turn():
    move_animals(rabbits)
    move_animals(wolves)
    hunt()
    print("Кроликов", len(rabbits))
    print("Волков", len(wolves))
    canvas.delete("all")
    for row in range(ROWS):
        for col in range(COLS):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE

            canvas.create_rectangle(
                x1, y1,
                x1 + CELL_SIZE, y1 + CELL_SIZE,
                outline = "black"
            )
    draw_animals() 

def draw_animals():
    for rabbit in rabbits:
        x = rabbit["x"] * CELL_SIZE
        y = rabbit["y"] * CELL_SIZE

        canvas.create_oval(
            x + 5, y + 5,
            x + CELL_SIZE - 5, y + CELL_SIZE - 5,
            fill = "violet"
        )
    for wolf in wolves:
        x = wolf["x"] * CELL_SIZE
        y = wolf["y"] * CELL_SIZE

        canvas.create_oval(
            x + 5, y + 5,
            x + CELL_SIZE - 5, y + CELL_SIZE - 5,
            fill = "green"
        )  
draw_animals()
button = tk.Button(root, text = "Отправить Ракеты на Киев", command = next_turn)
button.pack()
 
root.mainloop()
