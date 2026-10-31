import tkinter as tk

COLS = 30
ROWS = 15
CELL_SIZE = 25
import random
RABBIT_COUNT = 65
WOLF_COUNT = 40
rabbits = []
wolves = []
day = 0
max_AGE = 10

for i in range(RABBIT_COUNT):
    rabbit = {
        "x": random.randint(0, COLS - 1),
        "y": random.randint(0, ROWS - 1),
        "age": 0
    }
    rabbits.append(rabbit)

for i in range(WOLF_COUNT):
    wolf = {
        "x": random.randint(0,COLS - 1),
        "y": random.randint(0,ROWS - 1),
        "age": 0,
        "energy":  0
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
stats_label = tk.Label(root, text = "")
stats_label.pack()

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
                wolf["energy"] += 3
                break
def reproduce_rabbits():
    for rabbit in rabbits[:]:
        if random.random() < 0.05:
            new_rabbit = {
                "x": rabbit["x"],
                "y": rabbit["y"],
                "age": 0
            }
            rabbits.append(new_rabbit)
def age_animals():
   for wolf in wolves[:]:
       wolf["age"] += 1
       if wolf["age"] >= max_AGE:
           wolves.remove(wolf)
   for rabbit in rabbits[:]:
        rabbit["age"] += 1
        if rabbit["age"] >= max_AGE:
            rabbits.remove(rabbit)

def reproduce_wolves():
    for wolf in wolves[:]:
        if wolf["energy"] >= 3:
            chance = 0.15
        elif wolf["energy"] >= 1:
            chance = 0.02
        else:
            continue

        if random.random() < chance:
            new_wolf = {
                "x": wolf["x"],
                "y": wolf["y"],
                "age": 0,
                "energy": 0
            }
            wolf["energy"] -= 2
            wolves.append(new_wolf)
def wolf_hunger():
    for wolf in wolves[:]:
        wolf["energy"] -= 1
        if wolf["energy"] < 0:
            wolves.remove(wolf)



def update_stats():
    stats_label.config(
        text = f"День: {day}| Кролики: {len(rabbits)}| Волки: {len(wolves)}"
    )

def next_turn():
    global day
    day += 1
    move_animals(rabbits)
    move_animals(wolves)
    hunt()
    wolf_hunger()
    reproduce_rabbits()
    reproduce_wolves()
    age_animals()
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
    update_stats() 

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
update_stats()
draw_animals()
button = tk.Button(root, text = "Отправить Ракеты на Киев", command = next_turn)
button.pack()
update_stats()
root.mainloop()
