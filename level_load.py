import json
import os

path = "config/levels.json"
with open(path, 'r') as lvls:
    levels = json.load(lvls)

# level_names = [levels[level] for level in levels]
# print(level_names)


def load_map(level_name):
    if level_name in levels.keys():
        return Level(levels[level_name])


class Level:
    def __init__(self, level_map):
        # load instance variables set to the values in the loaded dictionary for the level
        self.name = level_map['name']
        self.x_bound = level_map['x_bound']
        self.y_bound = level_map['y_bound']
        self.collisions = level_map['collisions']
        self.spawn = level_map['spawn_pos']
        self.spawn_x = self.spawn['x']
        self.spawn_y = self.spawn['y']

