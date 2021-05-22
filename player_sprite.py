import arcade
import random
FRAMES_PER_UPDATE = 5
FPU = FRAMES_PER_UPDATE
left = -1
right = 1


class Inventory:
    def __init__(self, size):
        self.items = []
        self.max_size = size

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def get(self):
        return self.items

    def get_len(self):
        return len(self.items)

    def display(self):
        return '\n'.join([f"{i}. {item.name}" for i, item in enumerate(self.items)])


class Player(arcade.Sprite):
    def __init__(self, x, y, scale, inv: Inventory):
        super().__init__(scale=scale)
        # path to texture folder
        texture_path = "resources/sprites/Dungeon_Character_2/sprite_01.png"
        self.textures = arcade.load_texture_pair(texture_path)
        self.texture = self.textures[1]
        self.center_x, self.center_y = x, y
        self.direction = 1
        self.holding_candle = False
        self.candle = None
        self.inv = inv

    def update(self):
        # self.center_x += self.change_x
        # self.center_y += self.change_y
        if self.change_x > 0.1:
            self.direction = 1
        if self.change_x < -0.1:
            self.direction = -1
        # if self.change_y > 0:
        #     self.direction = 0
        # elif self.change_y < 0:
        #     self.direction = 2

        if self.direction == 1:
            self.texture = self.textures[0]
        elif self.direction == -1:
            self.texture = self.textures[1]

    def move_x(self, x_speed):
        self.change_x = x_speed

    def move_y(self, y_speed):
        self.change_y = y_speed

    def set_direction(self, direction):
        self.direction = direction

    def set_candle(self, candle_object):
        self.candle = candle_object

    def toggle_candle(self):
        if self.holding_candle:
            self.holding_candle = False
        else:
            self.holding_candle = True
            self.candle.show()

    def collect(self, item):
        self.inv.add(item)
        vowels = ['a', 'e', 'i', 'o', 'u']
        variants = ["picked up", "found", "discovered", "stumbled upon"]
        variant = random.choice(variants)
        if item.name[0].lower() in vowels:
            pickup_text = f"You {variant} an {item.name}!"
        else:
            pickup_text = f"You {variant} an {item.name}!"

        return pickup_text

