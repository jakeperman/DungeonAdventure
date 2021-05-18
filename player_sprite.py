import arcade
FRAMES_PER_UPDATE = 5
FPU = FRAMES_PER_UPDATE
left = -1
right = 1


class Player(arcade.Sprite):
    def __init__(self, x, y, scale):
        super().__init__(scale=scale)
        # path to texture folder
        texture_path = "resources/sprites/Dungeon_Character_2/sprite_01.png"
        self.textures = arcade.load_texture_pair(texture_path)
        self.texture = self.textures[1]
        self.center_x, self.center_y = x, y
        self.direction = 1
        self.holding_candle = False
        self.candle = None

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

    # TODO: add player lantern with limited fuel
