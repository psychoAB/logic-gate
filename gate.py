import arcade

INPUT_GATE = 0
OUTPUT_GATE = 1
NOT_GATE = 2
AND_GATE = 3
OR_GATE = 4

IMAGE_FILENAME = [None, None, None, None, None]
IMAGE_FILENAME[INPUT_GATE] = 'images/input_gate.png'
IMAGE_FILENAME[OR_GATE] = 'images/or_gate.png'

class SpriteModel(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        x =  kwargs.pop('x', None)
        y =  kwargs.pop('y', None)
        self.world = kwargs.pop('world', None)

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

    def is_point_intersect_with_range(self, x, y, left_margin, right_margin, up_margin, down_margin):
        self.update()
        return x >= left_margin and x <= right_margin and y >= down_margin and y <= up_margin

    def is_point_intersect_with_output_of_gate(self, x, y, plugged_gate):
        return x >= plugged_gate.output_left_margin and x <= plugged_gate.output_right_margin and y >= plugged_gate.output_down_margin and y <= plugged_gate.output_up_margin

    def is_mouse_on(self, x, y):
        self.update()
        return x >= self.texture_left_margin and x <= self.texture_right_margin and y >= self.texture_down_margin and y <= self.texture_up_margin

class InputGateSprite(SpriteModel):
    def __init__(self, *args, **kwargs):
        args = (IMAGE_FILENAME[INPUT_GATE],) + args

        self.output = True
        self.gate_type = INPUT_GATE

        super().__init__(*args, ** kwargs)

    def update(self):
        super().update()

        self.output_left_margin = self.center_x - 8
        self.output_right_margin = self.center_x + 10
        self.output_down_margin = self.center_y + 28
        self.output_up_margin = self.center_y + 40

    def get_output(self):
        return self.output

    def set_output(self, output):
        self.output = output

class OrGateSprite(SpriteModel):
    def __init__(self, *args, **kwargs):
        self.is_left_input_plugged = False
        self.is_right_input_plugged = False

        args = (IMAGE_FILENAME[OR_GATE],) + args

        self.output = None
        self.left_input = False
        self.right_input = False
        self.gate_type = OR_GATE

        super().__init__(*args, ** kwargs)


    def update(self):
        super().update()

        self.output_left_margin = self.center_x - 8
        self.output_right_margin = self.center_x + 10
        self.output_down_margin = self.center_y + 28
        self.output_up_margin = self.center_y + 40

        self.left_input_left_margin = self.center_x - 20
        self.left_input_right_margin = self.center_x - 8
        self.right_input_left_margin = self.center_x + 10
        self.right_input_right_margin = self.center_x + 22
        self.input_down_margin = self.center_y - 47
        self.input_up_margin = self.center_y - 35
        self.center_x_left_input = self.left_input_left_margin - abs(self.left_input_left_margin - self.left_input_right_margin) / 2
        self.center_x_right_input = self.right_input_left_margin - abs(self.right_input_left_margin - self.right_input_right_margin) / 2
        self.center_y_input = self.input_up_margin - abs(self.input_down_margin - self.input_up_margin) / 2
        
        self.is_left_input_plugged = False
        self.is_right_input_plugged = False
        for gate_sprite in self.world.gate_sprites:
            if gate_sprite != self:
                self.input_plugged(gate_sprite)

        if not self.is_left_input_plugged:
            self.left_input = 0

        if not self.is_right_input_plugged:
            self.right_input = 0

    def input_plugged(self, plugged_gate):
        if self.is_point_intersect_with_output_of_gate(self.center_x_left_input, self.center_y_input, plugged_gate):
            self.left_input = plugged_gate.output
            self.is_left_input_plugged = True
        if self.is_point_intersect_with_output_of_gate(self.center_x_right_input, self.center_y_input, plugged_gate):
            self.right_input = plugged_gate.output
            self.is_right_input_plugged = True

    def get_output(self):
        self.output =  self.left_input | self.right_input
        return self.output

    def set_input(self, left_input = None, right_input = None):
        if left_input != None:
            self.left_input = left_input
        if right_input != None:
            self.right_input = right_input
