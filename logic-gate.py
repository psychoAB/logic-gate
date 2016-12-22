#!/usr/bin/python3

import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

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

class LogicGateGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE) 

        main_input_gate = InputGateSprite(x = 50, y = 100)
        main_or_gate = OrGateSprite(x = 125, y = 89)

        self.main_gate_sprites = [None, None, None, None, None, None]
        self.main_gate_sprites[INPUT_GATE] = main_input_gate
        self.main_gate_sprites[OR_GATE] = main_or_gate

        self.gate_sprites = []
        self.dragging = False

    def on_draw(self):
        arcade.start_render()

        for main_gate_sprite in self.main_gate_sprites:
            if main_gate_sprite != None:
                main_gate_sprite.draw()

        for gate_sprite in self.gate_sprites:
            gate_sprite.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        #print(str(x) + " " + str(y))
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.dragging:
            for gate_sprite in self.gate_sprites:
                if gate_sprite.is_mouse_on(x, y):
                    gate_sprite.set_position(x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.dragging = True

            for main_gate_sprite in self.main_gate_sprites:
                if main_gate_sprite != None:
                    if main_gate_sprite.is_mouse_on(x, y):
                        if main_gate_sprite.gate_type == INPUT_GATE:
                            new_gate = InputGateSprite(x = x , y = y)
                        if main_gate_sprite.gate_type == OR_GATE:
                            new_gate = OrGateSprite(x = x , y = y)
                        self.gate_sprites.append(new_gate)

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.dragging = False

if __name__ == '__main__':
    window = LogicGateGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
