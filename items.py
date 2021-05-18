import arcade
import time

class UnlitTorch(arcade.Sprite):
    def __init__(self, x, y, scale):
        super(UnlitTorch, self).__init__("resources/sprites/Dungeon_Tileset/sprite_092.png", scale, center_x=x, center_y=y)


class Torch(arcade.AnimatedTimeBasedSprite):
    def __init__(self, x, y, scale):
        super(Torch, self).__init__("resources/sprites/items and trap_animation/torch/torch_00.png", scale=scale, center_x=x, center_y=y)
        path = "resources/sprites/items and trap_animation/torch/"
        frames = [arcade.AnimationKeyframe(123, 125, arcade.load_texture(f"{path}torch_0{i}.png")) for i in range(4)]
        self.frames = frames


class SideTorch(arcade.AnimatedTimeBasedSprite):
    def __init__(self, x, y, flipped=False):
        super(SideTorch, self).__init__("resources/sprites/items and trap_animation/torch/wall_torch_00.png", center_x=x, center_y=y)
        path = "resources/sprites/items and trap_animation/torch/"
        frames = [arcade.AnimationKeyframe(123, 125, arcade.load_texture(f"{path}wall_torch_0{i}.png", mirrored=flipped)) for i in range(4)]
        self.frames = frames


class Candle(arcade.AnimatedTimeBasedSprite):
    def __init__(self, x, y, scale, flipped):
        super(Candle, self).__init__("resources/sprites/items and trap_animation/torch/candle_00.png", center_x=x, center_y=y, scale=scale)
        path = "resources/sprites/items and trap_animation/torch/"
        frames = [arcade.AnimationKeyframe(123, 125, arcade.load_texture(f"{path}candle_0{i}.png", mirrored=flipped)) for i in range(4)]
        self.frames = frames
        self.fuel_timer = time.time()
        self.fuel_level = 99

    def update(self):
        if time.time() - self.fuel_timer >= .5:
            self.fuel_level -= 1
            self.fuel_timer = time.time()

    def show(self):
        self.fuel_timer = time.time()


