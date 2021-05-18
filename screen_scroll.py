import arcade


class ScrollManager:
    def __init__(self, window: arcade.Window):
        self.width, self.height = window.width, window.height
        self.window = window

        # set default view positions
        self.right_view = self.width
        self.left_view = 0
        self.top_view = self.height
        self.bottom_view = 0

        # default screen limits

        # self.right_limit = self.left_limit = self.top_limit = self.bottom_limit = None
        self.limits = {"right": None, "left": None, "top": None, "bottom": None}
        self.views = {'right': self.width, 'left': 0, 'top': self.height - 300, 'bottom': -300}
        self.margins = {"right": 0, "left": 0, "top": 0, "bottom": 0}
        self.boundaries = {"right": None, "left": None, "top": None, "bottom": None}
        self.update_boundaries()
        self.changed = False
        self.update_views()

    def set_view_max(self, **kwargs):
        for arg, val in zip(kwargs.keys(), kwargs.values()):
            if arg in self.limits.keys():
                self.limits[arg] = val

    def set_view_change_margins(self, **kwargs):
        for arg, val in zip(kwargs.keys(), kwargs.values()):
            if arg in self.margins.keys():
                self.margins[arg] = val

    def set_view(self, view, value):
        if view in list(self.views.keys()):
            self.views[view] = value
            self.update_views()

    def check_views(self):
        view = self.views
        limits = self.limits
        right = False
        if self.limits['right'] is not None and self.views['right'] > limits['right']:
            self.views['left'] = limits['right'] - self.width
            self.views['right'] = self.views['left'] + self.width
            self.changed = True
            right = True

        elif limits['left'] is not None and view['left'] < limits['left']:
            view['left'] = limits['left']
            view['right'] = view['left'] + self.width
            self.changed = True

        if limits['top'] and view['top'] > limits['top']:
            view['bottom'] = limits['top'] - self.height
            view['top'] = view['bottom'] + self.height
            self.changed = True
        if limits['bottom'] is not None and view['bottom'] < limits['bottom']:
            view['bottom'] = limits['bottom']
            view['top'] = view['bottom'] + self.height
            self.changed = True

        return right

        # if self.changed:
        #     self.views['right'] = self.width + self.views['left']
        #     self.views['top'] = self.height + self.views['bottom']


    def update(self):


        self.changed = False
        player = self.window.player
        bounds = self.boundaries
        self.update_boundaries()
        # change left and right
        if player.left < bounds['left']:
            # print(f"left tham: {player.center_x - bounds['left']}")
            self.change_view("left", player.center_x - bounds['left'])
        elif player.right > bounds['right']:
            # self.change_view("left", player.right - bounds['right'])
            self.change_view("left", player.center_x - bounds['right'])

        # change top and bottom
        if player.top > bounds['top']:
            self.change_view("bottom", player.center_y - bounds['top'])
        elif player.bottom < bounds['bottom']:
            self.change_view("bottom", player.center_y - bounds['bottom'])

        self.check_views()

        if self.changed:
            self.update_views()



    def update_views(self):
        self.window.set_viewport(self.views['left'], self.views['right'], self.views['bottom'], self.views['top'])

    def get_views(self):
        return self.views

    def get_view(self, view):
        if view in list(self.views.keys()):
            return self.views[view]

    def output_values(self):
        print("-"*50)
        print(f"views: {self.views}")
        print(f"margins:{self.margins}")
        print(f"boundaries: {self.boundaries}")
        print(f"limits: {self.limits}")

    def update_boundaries(self):
        self.boundaries["right"] = self.views["right"] - self.margins["right"]
        self.boundaries["left"] = self.views["left"] + self.margins["left"]
        self.boundaries["top"] = self.views["top"] - self.margins["top"]
        self.boundaries["bottom"] = self.views["bottom"] + self.margins["bottom"]
        if self.boundaries['left'] > self.boundaries['right']:
            # print("bound diff", self.boundaries['left'] - self.boundaries['right'])
            pass
    def change_view(self, view, amount):
        self.views[view] += amount
        self.views['right'] = self.width + self.views['left']
        self.views['top'] = self.height + self.views['bottom']

        self.changed = True

        pass
    def decrease_view(self):
        pass

