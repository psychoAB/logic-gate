import arcade

INPUT_GATE = 0
OUTPUT_GATE = 1
NOT_GATE = 2
AND_GATE = 3
OR_GATE = 4

IMAGE_FILENAME = [None, None, None, None, None, None]
IMAGE_FILENAME[INPUT_GATE] = 'images/input_gate.png'
IMAGE_FILENAME[OR_GATE] = 'images/or_gate.png'

class SpriteModel(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        x =  kwargs.pop('x', None)
        y =  kwargs.pop('y', None)

        super().__init__(*args, **kwargs)

        self.set_position(x, y)
        self.update()

    def update(self):
        super().update()

        sprite_texture = self.textures[0]

        self.texture_left_margin = self.center_x - sprite_texture.width / 2
        self.texture_right_margin = self.center_x + sprite_texture.width / 2
        self.texture_down_margin = self.center_y - sprite_texture.height / 2
        self.texture_up_margin = self.center_y + sprite_texture.height / 2

    def is_mouse_on(self, x, y):
        self.update()
        return x >= self.texture_left_margin and x <= self.texture_right_margin and y >= self.texture_down_margin and y <= self.texture_up_margin

class InputGateSprite(SpriteModel):
    def __init__(self, *args, **kwargs):
        args = (IMAGE_FILENAME[INPUT_GATE],) + args
        super().__init__(*args, ** kwargs)

        self.output = None
        self.gate_type = INPUT_GATE

    def update(self):
        super().update()

        self.output_left_margin = self.center_x - 8
        self.output_right_margin = self.center_x + 10
        self.output_down_margin = self.center_y + 28
        self.output_up_margin = self.center_y + 40

class OrGateSprite(SpriteModel):
    def __init__(self, *args, **kwargs):
        args = (IMAGE_FILENAME[OR_GATE],) + args
        super().__init__(*args, ** kwargs)

        self.output = None
        self.left_input = None
        self.right_input = None
        self.gate_type = OR_GATE

    def update(self):
        super().update()

        self.output_left_margin = self.center_x - 8
        self.output_right_margin = self.center_x + 10
        self.output_down_margin = self.center_y + 28
        self.output_up_margin = self.center_y + 40

        self.left_input_left_margin = self.center_x - 20
        self.left_input_right_margin = self.center_x - 8
        self.right_input_left_margin = self.center_x + 10
        self.right_input_right_margin = self.center_x +22
        self.input_down_margin = self.center_y - 47
        self.input_up_margin = self.center_y - 35
