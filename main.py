import arcade
import screen_scroll
import player_sprite
from arcade.experimental.lights import Light, LightLayer
import items
import random
import time
import itertools
from old import backend

SW, SH = 1600, 900
up = 0
right = 1
down = 2
left = 3
SCALE = 1
MOVEMENT_SPEED = 5 * SCALE
AMBIENT_COLOR = (10, 10, 10)
TORCH_LIGHT = (255, 217, 140)
TORCH_RADIUS = 200 * SCALE
ACTION_RANGE = 80 * SCALE
# TORCH_RADI = [r * SCALE for r in [175, 190, 210, 225, 205, 169, 180, 215]]
TORCH_RADI = [random.randrange(165, 230) * SCALE for r in range(50)]
CANDLE_RADI = [random.randrange(325, 425) * SCALE for x in range(50)]

# TODO: Grid Based Inventory
# TODO: Immersive Hotbar, (1-9), Opaque, hover next to player

class Dialogue:
    def __init__(self, *args, delay=1):
        # self.text = [text for t in text]
        self.text = ' '.join(args)
        self.index = 0
        self.print_index = 0
        self.delay = delay
        self.printing = True

    def advance(self):
        self.index += 1 / self.delay
        # print(self.index)
        self.print_index = int(self.index)
        if self.print_index > len(self.text):
            self.index = len(self.text)
            self.printing = False

    def output(self):
        return self.text[:self.print_index]


class TorchLight(Light):
    def __init__(self, x, y, radius):
        super(TorchLight, self).__init__(x, y, radius, TORCH_LIGHT, 'soft')


class Game(arcade.Window):
    def __init__(self):
        super(Game, self).__init__(SW, SH, "Adventure Dungeon")
        map = arcade.tilemap.read_tmx("resources/dungeon.tmx")

        # process each layer from tilemap and create a spritelist from it
        self.ground_list = arcade.tilemap.process_layer(map, "floor", scaling=SCALE)
        self.wall_list = arcade.tilemap.process_layer(map, "walls", scaling=SCALE)
        self.background = arcade.tilemap.process_layer(map, "bg", scaling=SCALE)
        self.doors = arcade.tilemap.process_layer(map, "doors", scaling=SCALE)
        self.light_list = arcade.tilemap.process_layer(map, "lit_lights", scaling=SCALE)
        self.perma_torches = arcade.tilemap.process_layer(map, "perma_lights", scaling=SCALE)
        self.unlit_lights = arcade.tilemap.process_layer(map, "unlit_lights", scaling=SCALE)
        self.chests = arcade.tilemap.process_layer(map, "chests", scaling=SCALE)
        self.decor = arcade.tilemap.process_layer(map, "decor", scaling=SCALE)

        # viewport scroll manager
        self.scroll_manager = screen_scroll.ScrollManager(self)

        # create the player
        self.player = player_sprite.Player(2816*SCALE, 192*SCALE, SCALE, player_sprite.Inventory(10))
        # initialize control values
        self.controls = {'w': MOVEMENT_SPEED, 'a': -MOVEMENT_SPEED, 's': -MOVEMENT_SPEED, 'd': MOVEMENT_SPEED}
        self.keys_pressed = []
        # mouse position
        self.mouse_pos = 0
        # scroll margin (how close player needs to be to the edge of view for it to scroll)
        margin_lr = SW/2 - self.player.width/2
        margin_tb = SH/2 - self.player.height/2
        # set the margins
        self.scroll_manager.set_view_change_margins(right=margin_lr, left=margin_lr, top=margin_tb, bottom=margin_tb)
        # set the initial view
        self.scroll_manager.set_view("right", 2208)
        self.scroll_manager.set_view("left", 2208 - SW)
        self.scroll_manager.set_view("bottom", self.player.center_y - (SH/2))
        self.scroll_manager.set_view("top", self.player.center_y + (SH/2))

        self.hit_wall = False
        # create physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.wall_list)
        self.light_index = 0
        # self.textures = arcade.load_spritesheet("resources/dungeon_sprites.png", 16, 16, 16, 72)
        # print(len(self.textures))

        # for lighting
        self.light_layer = None
        self.player_light = None
        self.torches = {}
        self.text = Dialogue("Welcome to Adventure Game!", delay=3)
        self.candle = None
        self.candle_light = None
        self.start_time = time.time()

        candle = items.Candle(self.player.right, self.player.center_y, .5, False)
        self.player.set_candle(candle)

        # generate loot
        self.room_loot = backend.gen_loot()
        self.show_text = False

        # inv show
        self.show_inv = False
        self.setup()

    def setup(self):
        # create the light layer (width and height of screen)
        self.light_layer = LightLayer(SW, SH)
        # set background color
        self.light_layer.set_background_color(arcade.color.BLACK)

        # create the player light
        radius = 100 * SCALE
        mode = 'soft'
        color = arcade.csscolor.WHITE
        self.player_light = Light(0, 0, radius, color, mode)
        # add the light layer
        self.light_layer.add(self.player_light)
        # create a light for each torch
        for torch in self.light_list:
            light = TorchLight(torch.center_x, torch.center_y, TORCH_RADIUS)
            self.light_layer.add(light)
            self.torches[torch] = light
        # lighting for torches that cant be unlit
        for torch in self.perma_torches:
            light = TorchLight(torch.center_x, torch.center_y, TORCH_RADIUS)
            self.light_layer.add(light)
            self.torches[torch] = light


        # add loot to chests
        loot = []
        for room in self.room_loot:
            loot += room
        for chest, loot in zip(self.chests, loot):
            chest.loot = loot



    def on_draw(self):
        arcade.start_render()
        # draw background (but dont illuminate it)
        self.background.draw()
        # draw all the sprites in light layer (lighting will illuminate them)
        with self.light_layer:
            self.ground_list.draw()
            self.doors.draw()
            self.wall_list.draw()
            self.chests.draw()
            self.decor.draw()
            self.player.draw()
            self.light_list.draw()
            self.unlit_lights.draw()
            self.perma_torches.draw()

        # draw the actual light layer
        self.light_layer.draw(ambient_color=AMBIENT_COLOR)


        if self.candle:
            fuel_len = self.candle.fuel_level / 2
            if self.candle_light.radius > 1:
                # draw the candle fuel bar above player
                arcade.draw_lrtb_rectangle_filled(self.player.left, self.player.left + fuel_len + 1, self.player.top + 10, self.player.top + 5, (255, 213, 105))
        # draw tutorial text for the first 5 seconds after startup
        if time.time() - self.start_time < 5:
            x = self.scroll_manager.get_view('right')
            y = self.scroll_manager.get_view('bottom')
            arcade.draw_text("press 'space' to toggle your candle", x - (SW / 2), y + 225, arcade.color.CREAM, 20,
                             anchor_x='center')
            arcade.draw_text("press 'q' to toggle torches on the wall (some torches can't be toggled)", x - (SW / 2), y + 250,
                             arcade.color.CREAM, 20, anchor_x='center')

        # show dialogue text
        if self.show_text:
            x = self.scroll_manager.get_view('right')
            y = self.scroll_manager.get_view('bottom')
            arcade.draw_text(self.text.output(), x - (SW/2), y + 200, arcade.color.CREAM, 20, anchor_x='center', align='center')

        if self.show_inv:
            inv_text = self.player.inv.display()
            leng = self.player.inv.get_len() * 20
            top = self.player.center_y + leng/2
            bottom = self.player.center_y - leng/2
            # ban = arcade.Sprite("resources/sprites/Dungeon_Tileset/sprite_074.png", self.player.right + 10, self.player.center_y, image_height=leng, image_width=150)
            # ban.draw()
            arcade.draw_lrtb_rectangle_filled(self.player.right + 10, self.player.center_x + 200, top, bottom, (118, 74, 45))
            arcade.draw_text(inv_text, self.player.right + 15, self.player.center_y, (255, 253, 208, 200), 11,
                             anchor_x='left', anchor_y='center', align='left', font_name='Chalkboard')




    def on_update(self, delta_time: float):
        # update physics engine
        self.physics_engine.update()
        self.decor.update_animation()
        if self.player.holding_candle:
            self.candle.update()
            # calculate ratio of remaining fuel
            fuel_ratio = self.candle.fuel_level / 100
            # set light radius progressively smaller as fuel runs out
            if fuel_ratio < .5:
                self.candle_light.radius = CANDLE_RADI[int(self.light_index)] - ((400 - (400 * fuel_ratio))/5)
            else:
                self.candle_light.radius = CANDLE_RADI[int(self.light_index)]
            # change candle position based on player direction
            if self.player.direction == 1:
                self.player.candle.position = self.player.right, self.player.center_y
            else:
                self.player.candle.position = self.player.left, self.player.center_y
            # set the position of light object equal to candles position
            self.candle_light.position = self.candle.position
            # if the candle runs out of fuel, disable it and re-enable players light source
            if self.candle.fuel_level <= 0:
                self.candle_light.radius = 0
                self.player_light.radius = 100

        # make player light follow
        self.player_light.position = self.player.position
        # update screen view
        self.scroll_manager.update()
        # vary the light radius of torches to simulate real fire
        for light in self.torches.values():
            light.radius = TORCH_RADI[int(self.light_index)]
        # increase light index by .1. only whole number indexes so every
        # 10 frames it will increase by a whole number and update
        self.light_index += .1
        if self.light_index >= len(TORCH_RADI):
            self.light_index = 0
        self.perma_torches.update_animation()
        self.light_list.update_animation()
        # update
        self.player.update()
        # update keys
        self.key_change()
        # advance dialogue text\
        if self.text:
            self.text.advance()


    # movement system
    def key_change(self):
        v_keys = 0
        h_keys = 0
        if self.keys_pressed:
            for key in self.keys_pressed:
                if key in 'ws':
                    self.player.move_y(self.controls[key])
                    v_keys += 1
                elif key in 'ad':
                    h_keys += 1
                    self.player.move_x(self.controls[key])
            if not v_keys:
                self.player.move_y(0)
            elif not h_keys:
                self.player.move_x(0)
        else:
            self.player.move_x(0)
            self.player.move_y(0)


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        light = arcade.get_sprites_at_point((x, y), self.unlit_lights)
        # if light:


    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        global SCALE

        key = chr(symbol)
        # if key in movement controls add to keys pressed
        if key in list(self.controls.keys()):
            self.keys_pressed.append(key)
        elif key == 'q':  # toggle torches on the wall on/off
            if not self.loot_chest():
                self.toggle_torch()

        elif key == 'e':
            if self.show_inv:
                self.show_inv = False
            else:
                self.show_inv = True

        elif symbol == arcade.key.SPACE and self.show_text:
            self.show_text = False
            self.text = None

        elif key == 'm':
            print("mouse_pos:", self.mouse_pos)
            print("playerpos:", self.player.position)
            self.scroll_manager.output_values()

        # toggle the players candle
        elif symbol == arcade.key.SPACE:
            # if the player is holding a candle, toggle it off
            if self.player.holding_candle:
                self.player.toggle_candle()  # toggle
                self.light_layer.remove(self.candle_light)  # remove light source
                self.perma_torches.remove(self.candle)  # remove from torches (it will not draw anymore)
                self.player_light.radius = 100 * SCALE # re-enable player default light
                self.candle = None  # set candle to None
            # if player isn't holding candle, toggle it on
            else:
                # toggle
                self.player.toggle_candle()
                # create lightsource object

                light = Light(self.player.candle.center_x, self.player.candle.center_y, 400 * SCALE, TORCH_LIGHT, 'soft')
                self.perma_torches.append(self.player.candle)  # add player candle to perma_torches (cant be toggled by pressing q)
                self.candle = self.player.candle  # set the candle to the players candle
                self.candle_light = light  # set candle light to light object
                self.player_light.radius = 0  # disable the players default light
                self.light_layer.add(self.candle_light)  # add light source to light layer

        self.key_change()

    def loot_chest(self):
        # get closest chest sprite
        chest = arcade.get_closest_sprite(self.player, self.chests)
        dist = chest[1]
        chest = chest[0]
        # if the chest is within range, loot it and display the contents
        if dist < ACTION_RANGE:
            item = chest.loot
            if item:
                # set show text to true and create new dialogue object
                self.show_text = True
                self.text = Dialogue(self.player.collect(item),'\n', item.description, delay=3)
                chest.loot = None
                return True
            else:
                # loot can only be found once
                self.show_text = True
                self.text = Dialogue(f"You already found the loot in this chest.")


    def toggle_torch(self):
        # get closest unlit torch
        unlit_torch = arcade.get_closest_sprite(self.player, self.unlit_lights)
        dist = unlit_torch[1]
        unlit_torch = unlit_torch[0]
        # if torch is within action range, turn it on
        if dist < ACTION_RANGE:
            # create new lit torch to replace unlit torch
            new_torch = items.Torch(unlit_torch.center_x, unlit_torch.center_y, SCALE)
            # get rid of unlit torch
            unlit_torch.kill()
            # add torch to list of torches
            self.light_list.append(new_torch)
            # create a new light source and assign it to the torch
            light = Light(new_torch.center_x, new_torch.center_y, TORCH_RADIUS, TORCH_LIGHT, 'soft')
            self.torches[new_torch] = light
            self.light_layer.add(light)
        else:
            lit_torch = arcade.get_closest_sprite(self.player, self.light_list)
            dist = lit_torch[1]
            lit_torch = lit_torch[0]
            # self.torches.pop(lit_torch)
            # if there isnt an unlit torch in range, but there is a lit torch, turn it off
            if dist < ACTION_RANGE:
                # make new unlit torch
                new_torch = items.UnlitTorch(lit_torch.center_x, lit_torch.center_y, SCALE)
                # get rid of light source
                light = self.torches[lit_torch]
                self.light_layer.remove(light)
                # get rid of lit torch and add unlit torch
                lit_torch.kill()
                self.unlit_lights.append(new_torch)


    def on_key_release(self, symbol: int, modifiers: int):
        key = chr(symbol)
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)

        self.key_change()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.mouse_pos = (x, y)


        pass



def main():
    game = Game()
    arcade.run()


if __name__ == "__main__":
    main()
